#!/usr/bin/env python3
""" 2022-02-22 - trcm - Do ISO 8601 time differences """

from datetime import datetime, timedelta
import sys


def title():
    """Print title"""
    print("Compare two ISO 8601 datetime strings (w/wo microseconds)")


def usage():
    """Print usage"""
    now_no_tz = datetime.now().isoformat()
    # '2022-02-23T19:03:05.057504'
    now = datetime.fromisoformat((str(now_no_tz) + "+00:00"))
    # '2022-02-23T19:03:05.057504+00:00'
    future = now + timedelta(seconds=1337)
    print(
        "\nUsage:\n"
        f"  {sys.argv[0]} now {future.isoformat()}\n"
        f"  {sys.argv[0]} {now.isoformat()} {future.isoformat()}\n"
        "\nReturns: [D day[s], ][H]H:MM:SS[.UUUUUU]"
    )


try:
    argv1 = sys.argv[1]
    argv2 = sys.argv[2]
    if "now" in argv1:
        # If using the keyword 'now', append UTC TZ
        dt1_no_tz = datetime.now()
        dt1 = datetime.fromisoformat((str(dt1_no_tz) + "+00:00"))
    else:
        if any(item in argv1[-6] for item in ["-", "+"]):
            dt1 = datetime.fromisoformat(argv1)
        else:
            # If no TZ in argument, append UTC TZ
            dt1_no_tz = datetime.fromisoformat(argv1)
            dt1 = datetime.fromisoformat((str(dt1_no_tz) + "+00:00"))
    if "now" in argv2:
        dt2_no_tz = datetime.now()
        dt2 = datetime.fromisoformat((str(dt2_no_tz) + "+00:00"))
    else:
        if any(item in argv2[-6] for item in ["-", "+"]):
            dt2 = datetime.fromisoformat(argv2)
        else:
            dt2_no_tz = datetime.fromisoformat(argv2)
            dt2 = datetime.fromisoformat((str(dt2_no_tz) + "+00:00"))
    diff = dt2 - dt1
except IndexError as e:
    title()
    usage()
    sys.exit(0)
except ValueError as e:
    print(e)
    usage()
    sys.exit(1)
else:
    print(f"timedelta= {str(diff)}")
    print(f"totalseconds= {diff.total_seconds()}")
