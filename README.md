# AttendanceW

*A WhatsApp bot that reminds our group whose turn it is to take Saturday attendance.*

Attendance rotates weekly through five of us, anchored to the week of March 16, 2026. The bot works out whose week it is and posts to the group chat through Green API. On Monday it names that person and the upcoming Saturday's date and asks everyone to like the message to confirm; on Saturday morning it sends a shorter "don't forget, today it's your turn" nudge.

It's just one stdlib Python script driven by GitHub Actions, which fires the Monday and Saturday crons at 16:00 UTC (noon Eastern in summer). A second `keepalive` workflow commits a timestamp on the 1st and 15th of each month, because GitHub disables scheduled workflows after 60 days without repo activity and these reminders need to keep running past then.
