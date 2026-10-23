import subprocess

APPLESCRIPT = r'''
tell application "System Events"
    set report to ""
    set appProcesses to every application process ¬
        whose visible is true and background only is false

    repeat with appProcess in appProcesses
        set appName to name of appProcess

        try
            set appWindows to every window of appProcess

            repeat with appWindow in appWindows
                try
                    if value of attribute "AXMinimized" of appWindow is false then
                        set value of attribute "AXMinimized" of appWindow to true
                        set report to report & appName & ": minimised a window" & linefeed
                    else
                        set report to report & appName & ": already minimised" & linefeed
                    end if
                on error errorMessage
                    set report to report & appName & ": FAILED — " & errorMessage & linefeed
                end try
            end repeat

        on error errorMessage
            set report to report & appName & ": FAILED — " & errorMessage & linefeed
        end try
    end repeat

    return report
end tell
'''


def minimize_all():
    try:
        result = subprocess.run(
            ["osascript", "-e", APPLESCRIPT],
            capture_output=True,
            text=True,
            timeout=20
        )

        if result.returncode == 0:
            print(result.stdout)
        else:
            print("AppleScript error:", result.stderr)

    except subprocess.TimeoutExpired:
        print("Operation timed out.")

    except OSError as error:
        print("Execution error:", error)


if __name__ == "__main__":
    minimize_all()