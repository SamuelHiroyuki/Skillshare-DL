import sys, os
from skillshare import Skillshare, splash

# or by class ID:
# dl.download_course_by_class_id('396830381')

def main():
    dl = Skillshare("PHPSESSID=be16420cdd9790f57c0fbade47f805ac")
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
