# TODO List for Project

## Bugs to Fix

### High Priority

1. **Application Exit Issue**
   - **Description**: Determine why the application does not stop running after the main program window is closed.
   - **Steps**:
     - Investigate the main event loop handling.
     - Check for any background threads or processes that might be preventing the application from exiting completely.

2. **Treeview Update Issue on Login**
   - **Description**: Resolve the issue where the treeview of products does not update immediately when a user logs in.
   - **Steps**:
     - Review the event handling after user login to ensure the product list is refreshed.
     - Verify the connection and data fetching logic from the database to the treeview.

## Features to Implement

- [ ] Add user role management.
- [ ] Implement logging for debugging and audit trails.

## General Improvements

- [ ] Optimize database queries.
- [ ] Refactor the user authentication flow.

---

## Notes
