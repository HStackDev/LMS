

# Software Requirements Specification (SRS)

## Library Management System (LMS)

### 1. Introduction

**Purpose:**
The Library Management System (LMS) automates book, member, and borrowing/return operations, reducing manual effort and providing quick access to library information.

**Scope:**

* Book & member management
* Borrowing & returning books
* Search functionality
* Basic report generation
* Support for Admin and Regular Users

**Intended Users:**

* Admin (Librarian): Full access
* Regular User (Member): Limited access

---

### 2. Features

| Feature ID | Feature Name          | Description                         |
| ---------- | --------------------- | ----------------------------------- |
| F1         | Book Management       | Add, edit, delete, view books       |
| F2         | Member Management     | Add, edit, delete, view members     |
| F3         | Borrowing & Returning | Record borrow/return transactions   |
| F4         | Search Books          | Search books by title, author, ISBN |
| F5         | Reports               | Generate borrowed/overdue reports   |

---

### 3. Functional Requirements

| ID   | Requirement                                            | Role        | Priority     |
| ---- | ------------------------------------------------------ | ----------- | ------------ |
| FR1  | Add new book (title, author, ISBN, category, quantity) | Admin       | Mandatory    |
| FR2  | Edit book details                                      | Admin       | Mandatory    |
| FR3  | Delete books                                           | Admin       | Mandatory    |
| FR4  | View list of all books                                 | Admin, User | Mandatory    |
| FR5  | Add new members                                        | Admin       | Mandatory    |
| FR6  | Edit member info                                       | Admin       | Nice-to-Have |
| FR7  | Delete members                                         | Admin       | Nice-to-Have |
| FR8  | View list of members                                   | Admin       | Mandatory    |
| FR9  | Record book borrowing with due date                    | Admin       | Mandatory    |
| FR10 | Record book return                                     | Admin       | Mandatory    |
| FR11 | Search books by title, author, ISBN                    | Admin, User | Mandatory    |
| FR12 | View own borrowing history                             | User        | Nice-to-Have |
| FR13 | Generate reports (borrowed/overdue)                    | Admin       | Nice-to-Have |

---

### 4. Non-Functional Requirements

| ID   | Requirement                          | Notes      | Priority     |
| ---- | ------------------------------------ | ---------- | ------------ |
| NFR1 | Simple, user-friendly interface      | Both roles | Mandatory    |
| NFR2 | Fast search & list (<2s)             | Both roles | Mandatory    |
| NFR3 | Authorization for admin tasks        | Admin      | Mandatory    |
| NFR4 | Reliable data storage & backup       | Both roles | Mandatory    |
| NFR5 | Easy system maintenance              | Both roles | Nice-to-Have |
| NFR6 | Secure login (password encryption)   | Both roles | Mandatory    |
| NFR7 | Handle multiple users simultaneously | Both roles | Nice-to-Have |

---

### 5. User Roles

| Role         | Description | Access                     |
| ------------ | ----------- | -------------------------- |
| Admin        | Librarian   | Full access                |
| Regular User | Member      | Search books, view history |

---

### 6. Use Case Diagram (Text Version)

```
Actors:
- Admin
- User
Use Cases:
- Admin: Add/Edit/Delete/View Books, Add/Edit/Delete/View Members, Borrow/Return Books, Generate Reports
- User: Search Books, View Borrowing History
```

### 7. MongoDB Schema Diagram

<img src="https://sdmntprpolandcentral.oaiusercontent.com/files/00000000-b1b0-620a-9b8f-6a0ef375ca11/raw?se=2025-10-05T00%3A27%3A00Z&sp=r&sv=2024-08-04&sr=b&scid=a747c18f-1c8f-5edb-9bf0-047f02e72f06&skoid=eb780365-537d-4279-a878-cae64e33aa9c&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-10-04T22%3A41%3A28Z&ske=2025-10-05T22%3A41%3A28Z&sks=b&skv=2024-08-04&sig=nklnyZVbT9egeBqtrYNPXEIrfQx2dQzao9h0mloU1Yw%3D">

---

### 8. Priority

* Mandatory: Must be implemented for MVP
* Nice-to-Have: Can be added later
