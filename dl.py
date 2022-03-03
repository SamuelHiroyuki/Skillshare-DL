import sys, os
from skillshare import Skillshare, splash

# or by class ID:
# dl = Skillshare("PHPSESSID=1c33be9de9fc2c0d588314a935770619")

def main():
    dl = Skillshare("PHPSESSID=1c33be9de9fc2c0d588314a935770619")
    course_url = sys.argv[1]
    dl.download_course_by_class_id('396830381')


if __name__ == "__main__":
    splash()
    main()
