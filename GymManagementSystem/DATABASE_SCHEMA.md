# API Documentation (Optional Reference)

This document describes the database models and relationships in the Gym Management System.

## Database Models

### 1. Admin
**Purpose**: System administrator accounts
```
- admin_id (Primary Key)
- name
- username (Unique)
- password (Hashed)
- contact_no
- email (Unique)
- created_at
```

### 2. Member
**Purpose**: Gym member central entity
```
- member_id (Primary Key)
- name
- dob (Date of birth)
- gender
- contact_no
- weight (kg)
- height (cm)
- health_issue
- goal
- join_date
- trainer_id (Foreign Key) → Trainer
- admin_id (Foreign Key) → Admin
```

### 3. Trainer
**Purpose**: Fitness trainer information
```
- trainer_id (Primary Key)
- name
- specialization
- contact_no
- shift_time
- email
- created_at
- members (Relationship: 1 Trainer → M Members)
```

### 4. Workout_Plan
**Purpose**: Exercise plans for fitness goals
```
- workout_id (Primary Key)
- goal
- description
- duration
- created_at
```

### 5. Diet
**Purpose**: Nutritional plans for members
```
- diet_id (Primary Key)
- member_id (Foreign Key) → Member
- goal
- meal_type (Breakfast/Lunch/Dinner/Snack)
- items
- created_at
```

### 6. Progress
**Purpose**: Fitness progress tracking
```
- progress_id (Primary Key)
- member_id (Foreign Key) → Member
- date
- weight
- bmi
- notes
- created_at
```

### 7. Attendance
**Purpose**: Member attendance records
```
- attendance_id (Primary Key)
- member_id (Foreign Key) → Member
- date
- status (Present/Absent/Leave)
- created_at
```

### 8. Payment
**Purpose**: Payment tracking
```
- payment_id (Primary Key)
- member_id (Foreign Key) → Member
- amount
- payment_date
- status (Paid/Pending/Failed)
- notes
- created_at
```

### 9. Notification
**Purpose**: System notifications for members
```
- notif_id (Primary Key)
- member_id (Foreign Key) → Member
- message
- date
- read_status
- created_at
```

## Relationships

### 1:M (One-to-Many)
- **Admin → Members**: 1 Admin manages M Members
- **Trainer → Members**: 1 Trainer guides M Members
- **Member → Progress**: 1 Member has M Progress records
- **Member → Attendance**: 1 Member has M Attendance records
- **Member → Payment**: 1 Member makes M Payments
- **Member → Notification**: 1 Member receives M Notifications
- **Member → Diet**: 1 Member follows M Diet plans

## Database Schema Visualization

```
┌─────────────┐
│   Admin     │
└──────┬──────┘
       │
       │ manages (1:M)
       ▼
┌──────────────────────────────────────┐
│            Member                    │
│ ├─ member_id (PK)                   │
│ ├─ name, dob, gender                │
│ ├─ contact_no, weight, height       │
│ ├─ health_issue, goal, join_date    │
│ ├─ trainer_id (FK) ─→ Trainer       │
│ └─ admin_id (FK) ─→ Admin           │
└──────┬──────────────────────────────┘
       │
       ├─→ Progress (1:M)
       ├─→ Attendance (1:M)
       ├─→ Payment (1:M) ─→ Notification (1:1 per payment)
       └─→ Diet (1:M)
```

## Sample Database Queries

### Get Member with Trainer
```
SELECT m.name, m.goal, t.name as trainer_name
FROM member m
LEFT JOIN trainer t ON m.trainer_id = t.trainer_id
```

### Get Member Progress (Recent)
```
SELECT * FROM progress
WHERE member_id = ? 
ORDER BY date DESC
LIMIT 10
```

### Get Payment Summary
```
SELECT 
    SUM(amount) as total_revenue,
    COUNT(CASE WHEN status='Paid' THEN 1 END) as paid_count,
    COUNT(CASE WHEN status='Pending' THEN 1 END) as pending_count
FROM payment
WHERE payment_date >= DATE('now', 'start of month')
```

### Get Attendance Report
```
SELECT 
    m.name,
    COUNT(*) as total_days,
    SUM(CASE WHEN status='Present' THEN 1 ELSE 0 END) as present_days
FROM attendance a
JOIN member m ON a.member_id = m.member_id
GROUP BY a.member_id
```

---

For more details, refer to README.md and SETUP_GUIDE.md
