# Attendance Reminder Bot

A small bot that reminds a WhatsApp group whose turn it is to take attendance each Saturday.

A group of five people takes turns taking attendance, one person per week. Instead of someone keeping track by hand, this bot works out whose week it is and posts a reminder to the group chat automatically. It runs on a schedule in the cloud, so nobody has to remember to start it.

## What it does

- Every Monday, it posts a message naming that week's person and the date of the coming Saturday, and asks the group to like the message to confirm.
- Every Saturday, it sends a short "don't forget, it's your turn today" reminder.
- It rotates through the group in a fixed order, one person per week.
- It can be run by hand in a "practice" mode that shows the message without sending it.

This is a small, single-purpose tool: one short script plus the scheduling setup that runs it.
