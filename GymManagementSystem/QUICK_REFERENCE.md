# 🚀 Gym Management System - Quick Reference Card

## 🔑 Login Credentials

| User Type | Username | Password | Dashboard URL |
|-----------|----------|----------|---------------|
| **Admin** | `admin` | `admin123` | `/dashboard` |
| **Member** | Self-register | Self-created | `/member/dashboard` |
| **Trainer** | Self-register | Self-created | `/trainer/dashboard` |

---

## 📍 Main URLs

### Authentication
- **Login**: `http://localhost:5000/login`
- **Logout**: `http://localhost:5000/logout`
- **Register Member**: `http://localhost:5000/register/member`
- **Register Trainer**: `http://localhost:5000/register/trainer`

### Dashboards
- **Admin**: `http://localhost:5000/dashboard`
- **Member**: `http://localhost:5000/member/dashboard`
- **Trainer**: `http://localhost:5000/trainer/dashboard`

### Core Features
- **View Slots**: `http://localhost:5000/slots`
- **Create Slot**: `http://localhost:5000/slot/add`
- **My Bookings**: `http://localhost:5000/bookings`
- **Manage Members**: `http://localhost:5000/members`
- **Manage Trainers**: `http://localhost:5000/trainers`

---

## 👥 User Capabilities

### 👨‍💼 What Admin Can Do
```
Login as Admin
↓
✓ View all members, trainers, payments, attendance
✓ Add/edit/delete members and trainers
✓ Create training slots (assign to trainers)
✓ View and manage all bookings
✓ Track system statistics
✓ Generate reports
```

### 👤 What Member Can Do
```
Register → Login as Member
↓
✓ View personal profile & BMI
✓ See assigned trainer details
✓ Browse available slots
✓ Book training slots
✓ View own bookings
✓ Track attendance history
✓ View diet plans from trainer
✓ See payment history
```

### 💪 What Trainer Can Do
```
Register → Login as Trainer
↓
✓ View assigned members only
✓ Create training slots
✓ Edit/delete own slots
✓ Mark member attendance
✓ Assign diet & workout plans
✓ View member details
✓ Monitor slot bookings
```

---

## 🎯 Quick Tasks

### Register as Member
1. Go to `/register/member`
2. Fill: Name, DOB, Gender, Contact, Weight, Height, Goal, Health Issues
3. Choose trainer (optional)
4. Create username & password
5. Click Register
6. Login with new credentials

### Book a Slot (Member)
1. Login as Member
2. Click "View & Book Slots"
3. Browse available slots
4. Click "Book Now"
5. Confirm booking
6. Get confirmation notification

### Create Training Slot (Trainer)
1. Login as Trainer
2. Go to Dashboard
3. Click "Create New Slot"
4. Fill: Name, Day, Time, Capacity, Description
5. Click Create
6. Slot available for member bookings

### Mark Attendance (Trainer)
1. Login as Trainer
2. Go to Dashboard
3. Click "📋" icon on member name
4. Select date and status
5. Save
6. Attendance recorded

### Assign Diet Plan (Trainer)
1. Login as Trainer
2. Go to Dashboard
3. Click "🍎" icon on member name
4. Select goal and meal type
5. Enter food items & instructions
6. Save
7. Member can view in dashboard

---

## 📊 Database Quick Reference

### User Models
```
Admin (existing)
├─ username, password, email, contact_no

User (members login)
├─ member_id (unique FK)
├─ username (unique)
├─ password (hashed)
├─ email (unique)

TrainerUser (trainers login)
├─ trainer_id (unique FK)
├─ username (unique)
├─ password (hashed)
├─ email (unique)
```

### Business Models
```
Slot (training classes/sessions)
├─ slot_id (PK)
├─ slot_name
├─ trainer_id (FK)
├─ day_of_week (Mon-Sun)
├─ start_time, end_time
├─ capacity (default 20)
├─ description

Booking (slot reservations)
├─ booking_id (PK)
├─ member_id (FK)
├─ slot_id (FK)
├─ booking_date
├─ status (Confirmed/Cancelled)

Member (existing - updated)
├─ Now links to User account
├─ Stores health info
├─ Tracks bookings
```

---

## 🎨 Template Structure

**New Templates Created:**
- `login.html` - Multi-user login
- `register_member.html` - Member registration
- `register_trainer.html` - Trainer registration
- `member_dashboard.html` - Member homepage
- `trainer_dashboard.html` - Trainer homepage
- `slots_list.html` - Browse slots
- `add_slot.html` - Create slot
- `edit_slot.html` - Edit slot
- `confirm_booking.html` - Confirm booking
- `bookings_list.html` - View bookings
- `trainer_add_attendance.html` - Mark attendance
- `trainer_assign_diet.html` - Assign diet

---

## 🔐 Access Control Rules

| Action | Admin | Member | Trainer |
|--------|-------|--------|---------|
| View own dashboard | ✓ | ✓ | ✓ |
| View all members | ✓ | ✗ | ✗ |
| View all trainers | ✓ | ✗ | ✗ |
| Create members | ✓ | ✗ | ✗ |
| Edit members | ✓ | ✗ | ✗ |
| Create slots | ✓ | ✗ | ✓ Own |
| Edit slots | ✓ | ✗ | ✓ Own |
| Book slots | ✗ | ✓ | ✗ |
| Mark attendance | ✓ | ✗ | ✓ Own members |
| Assign diet | ✓ | ✗ | ✓ Own members |
| View bookings | ✓ All | ✓ Own | ✗ |

---

## 🐛 Debug Commands

### Check if running
```bash
# System starts at 5000
http://localhost:5000/
```

### View database
```bash
# Database location
instance/gym_management.db
```

### Default Admin
```
Username: admin
Password: admin123
```

### Reset Database
```bash
# Delete and recreate
rm instance/gym_management.db
python app.py
```

---

## 📈 Feature Comparison

### Before Enhancement ❌
- Admin-only login
- No member bookings
- No trainer portal
- Limited member features

### After Enhancement ✅
- Multi-user login (Admin, Member, Trainer)
- Full booking system
- Trainer portal with member management
- Rich member dashboard
- Attendance tracking by trainers
- Diet plan assignments
- Real-time availability
- User registration system

---

## 🎯 Next Steps

### Immediate (Day 1)
1. Test admin login with default credentials
2. Register a test member
3. Register a test trainer
4. Create a slot
5. Book the slot as member

### Short-term (Week 1)
1. Populate sample data
2. Train staff on usage
3. Set business rules
4. Establish pricing

### Long-term (Month 1)
1. Integration with payment system
2. Email notification setup
3. Performance analytics
4. Mobile app development

---

## 📞 Troubleshooting

| Issue | Solution |
|-------|----------|
| Can't login | Verify user type selection, username, password |
| Can't book | Must be Member, check capacity, no duplicate books |
| Can't see members | Must be Admin or assigned trainer |
| Slot not showing | Admin must create + assign trainer |
| Database error | Run `python app.py` to reinitialize |

---

## ✨ Feature Highlights

🔐 **Secure**: Password hashing, role-based access  
📱 **User-Friendly**: Intuitive dashboards, clear workflows  
⚡ **Fast**: Optimized queries, responsive UI  
📊 **Comprehensive**: Attendance, diet, payments, progress  
🎯 **Goal-Oriented**: Customized experiences per user type  

---

**Version**: 2.0 (Enhanced with Multi-User & Booking)  
**Last Updated**: March 2026  
**Status**: ✅ Ready for Deployment
