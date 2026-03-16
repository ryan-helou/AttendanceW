#!/usr/bin/env python3
"""WhatsApp Attendance Reminder System.

Sends a group chat reminder via Green API.

Setup:
    1. Sign up at green-api.com and link your WhatsApp.
    2. Set env vars: GREEN_API_URL, GREEN_API_INSTANCE, GREEN_API_TOKEN, GROUP_CHAT_ID
    3. To find your group chat ID, use the Green API "getContacts" endpoint.

Usage:
    python reminder.py --day mon
    python reminder.py --day sat --dry-run
"""

import argparse
import datetime
import json
import os
import urllib.request
import urllib.error

ROTATION = ["Ryan", "Jona", "Aly", "Holy", "Julia"]
ROTATION_START_DATE = "2026-03-16"  # A Monday when Ryan is assigned


def get_current_person() -> str:
    start = datetime.date.fromisoformat(ROTATION_START_DATE)
    today = datetime.date.today()
    week_index = ((today - start).days // 7) % len(ROTATION)
    return ROTATION[week_index]


def get_saturday_date() -> str:
    today = datetime.date.today()
    days_until_sat = (5 - today.weekday()) % 7
    saturday = today + datetime.timedelta(days=days_until_sat)
    return saturday.strftime("%B %d")


def build_message(day: str, person: str) -> str:
    if day == "mon":
        sat_date = get_saturday_date()
        return (
            f"{person} will be taking attendance on Saturday {sat_date}. "
            f"Please like this message to confirm \U0001f601"
        )
    return f"Don't forget that today {person} will be taking attendance!"


def send_message(api_url: str, instance: str, token: str, chat_id: str, message: str) -> None:
    url = f"{api_url}/waInstance{instance}/sendMessage/{token}"
    payload = json.dumps({"chatId": chat_id, "message": message}).encode()

    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(req) as resp:
            body = json.loads(resp.read().decode())
            print(f"Sent: {body}")
    except urllib.error.HTTPError as e:
        print(f"Failed: {e.code} {e.read().decode()}")
        raise SystemExit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", required=True, choices=["mon", "sat"])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    person = get_current_person()
    message = build_message(args.day, person)

    print(f"Assigned: {person}")
    print(f"Message:  {message}")

    if args.dry_run:
        print("(dry run)")
        return

    api_url = os.environ["GREEN_API_URL"]
    instance = os.environ["GREEN_API_INSTANCE"]
    token = os.environ["GREEN_API_TOKEN"]
    chat_id = os.environ["GROUP_CHAT_ID"]

    send_message(api_url, instance, token, chat_id, message)
    print("Done.")


if __name__ == "__main__":
    main()
