# Markify
# University Attendance Management System (QR-Based)

## 📌 Project Overview
The **University Attendance Management System** is a web-based application designed to simplify and automate the process of taking student attendance using **QR codes**.  
Instead of manual roll calls, the system generates a **daily QR code** that students scan to mark their attendance securely and efficiently.

This project is developed as part of a **programming class group project**.

---

## 🎯 Objectives
- Automate student attendance tracking
- Reduce manual errors and proxy attendance
- Provide a fast and user-friendly attendance system
- Secure attendance using time-limited QR codes

---

## 🛠️ Features
- Admin/University can add students to the database
- Student information is stored automatically
- QR code is generated daily for attendance
- QR code expires after a specified time
- Students scan the QR code to access the attendance page
- Students submit:
  - Name  
  - Student ID  
  - Date (auto-filled or selected)
- System validates student details
- Attendance is marked and stored in the database

---

## 🧑‍💻 System Workflow
1. University/Admin logs into the web application
2. Admin adds students to the database
3. System generates a QR code for the day
4. Students scan the QR code
5. QR redirects students to the attendance form
6. Students enter required details
7. System validates the student
8. Attendance is recorded in the database
9. QR code expires after the set time

---

## 🗄️ Database Structure (Example)
**Students Table**
- student_id (Primary Key)
- name
- department
- email

**Attendance Table**
- attendance_id (Primary Key)
- student_id (Foreign Key)
- date
- status (Present/Absent)
- timestamp

---

## 🔐 Security Features
- Time-limited QR codes
- Student ID validation
- Prevents multiple attendance submissions
- Attendance only allowed during active QR session

---

## 🧰 Technologies Used
- Frontend: HTML, CSS, JavaScript
- Backend: (e.g. Node.js / PHP / Python Flask)
- Database: MySQL / MongoDB
- QR Code Generator Library
- Web Server: (e.g. Apache / Express)

---

## 🚀 Future Enhancements
- Face recognition for attendance
- Mobile application version
- Admin dashboard with analytics
- Email/SMS notifications
- Role-based authentication (Admin, Lecturer, Student)

---

## 👥 Team Members
- Member 1 – Frontend Development  
- Member 2 – Backend Development  
- Member 3 – Database Design  
- Member 4 – QR Code & Validation Logic  

---

## 📄 License
This project is developed for educational purposes only.

---

## ✅ Conclusion
The QR-Based Attendance Management System provides a modern, efficient, and secure solution for managing university attendance. It minimizes manual work, saves time, and improves accuracy.

