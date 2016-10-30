#!/usr/bin/env python

# Main logic file for Commander.

from DBManager import DBManager
import argparse

def main():
    parser = argparse.ArgumentParser(description='Process arguments for Commander')
    parser.add_argument('-a', '--add', nargs='*', help="Add a command to the database")
    parser.add_argument('-d', '--delete', help="Delete a command from the database.", type=int)
    parser.add_argument('-s', '--search', help="Search for a command based on ID.")

    args = parser.parse_args()

    connector = DBManager('commands')

    if args.search:
        if args.search == "all":
            print connector.show_all_records()
        else:
            print connector.show_record_by_id(args.search)
    elif args.delete:
        print connector.del_record_by_id(args.delete)
    elif args.add:
        print connector.add_record(args.add)
    else:
        parser.print_help()
main()


