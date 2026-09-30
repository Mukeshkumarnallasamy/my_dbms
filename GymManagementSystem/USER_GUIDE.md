# 📚 User Guide - How to Use Gym Management System

Complete step-by-step guide on how to perform all common tasks.

---

## 🚀 GETTING STARTED

### Step 1: Start the Application
**Windows**: Double-click `run.bat`
**Mac/Linux**: Run `./run.sh`

### Step 2: Login
- Open: `http://localhost:5000`
- Username: `admin`
- Password: `admin123`

### Step 3: You're in the Dashboard
- See total members, trainers, and revenue
- Click any menu to start managing

---

## 👥 MANAGING MEMBERS

### CREATE A NEW MEMBER (with Member ID Auto-Generated)

**Step-by-Step:**

1. **Click**: `Members` in top navigation
2. **Click**: `+ Add New Member` button
3. **Fill the form** with these details:

```
📋 REQUIRED FIELDS (marked with *)
├─ Full Name *              → John Doe
├─ Date of Birth *          → 1995-05-15
├─ Gender *                 → Male / Female / Other
├─ Contact Number *         → 9876543210
├─ Weight (kg) *            → 75.5
├─ Height (cm) *            → 175
├─ Fitness Goal *           → Weight Loss / Muscle Gain / Endurance / Flexibility
├─ Join Date *              → 2026-02-14
│
📝 OPTIONAL FIELDS
├─ Health Issues            → "None" or specific issues (e.g., "Back pain")
├─ Assign Trainer           → Select from dropdown (optional)
```

4. **Member ID is created automatically** when you click "Add Member"
5. **Success message** appears
6. Member now appears in Members List

✅ **Member ID Example**: The system assigns ID 1, 2, 3... automatically

---

### VIEW MEMBER PROFILE (Complete Information)

**Step-by-Step:**

1. Click: `Members` in menu
2. Find member in the list
3. Click: `View` button

**You'll see:**

```
📌 MEMBER DETAILS TAB (First Tab - Always Open)
├─ Member ID                → Auto-generated (e.g., #1)
├─ Name                     → John Doe
├─ Gender                   → Male
├─ Contact                  → 9876543210
├─ Join Date                → 2026-02-14
├─ Fitness Goal             → Weight Loss
├─ Health Issues            → None or listed
├─ Assigned Trainer         → John Smith (Strength Training)
│
📊 PHYSICAL ATTRIBUTES
├─ Weight                   → 75.5 kg
├─ Height                   → 175 cm
├─ BMI (Auto-Calculated)    → 24.57 ✓
```

---

## 📊 WEIGHT TRACKING & PERSONAL DETAILS

### HOW WEIGHT TRACKING WORKS

**Automatic BMI Calculation:**
- BMI = Weight (kg) / (Height in meters)²
- System calculates automatically
- Tracks changes over time

**Step-by-Step to Record Weight:**

1. Go to: Member Profile
2. Click: `Progress` tab
3. Click: `+ Add Progress` button
4. Fill form:

```
📋 RECORD PROGRESS FORM
├─ Date *                   → Select date (e.g., today: 2026-02-14)
├─ Weight (kg) *            → Enter current weight (e.g., 73.5)
├─ Notes (Optional)         → Add comments (e.g., "Lost 2kg this week!")
│
✅ BMI CALCULATED AUTOMATICALLY
└─ Shows: 24.06 (updated from previous)
```

5. Click: `Record Progress`
6. View progress in `Progress` tab

**Example Progress History:**
```
Date       │ Weight │ BMI   │ Notes
2026-02-14 │ 73.5   │ 24.06 │ Lost 2kg this week!
2026-02-07 │ 75.5   │ 24.57 │ Started gym routine
2026-01-31 │ 78.0   │ 25.45 │ Initial weight
```

### VIEW PERSONAL DETAILS

To see/edit personal details:

1. **To View**: Click `View` button in Members list → See all details
2. **To Edit**: Click `Edit` button in Members list
3. **Update** any of these:
   - Name
   - Gender
   - Contact Number
   - Weight
   - Height
   - Health Issues
   - Fitness Goal
   - Trainer Assignment
4. Click: `Update Member`

---

## 🏋️ TRAINER ALLOCATION

### STEP 1: CREATE TRAINERS FIRST

**Add Trainer:**

1. Click: `Trainers` in menu
2. Click: `+ Add New Trainer`
3. Fill form:

```
📋 TRAINER INFORMATION
├─ Full Name *              → Sarah Johnson
├─ Email                    → sarah@gym.com
├─ Specialization *         → Strength Training / Cardio / Yoga / CrossFit
├─ Contact Number *         → 9876543211
├─ Shift Time *             → 6 AM - 12 PM / 12 PM - 6 PM / 6 PM - 10 PM / Full Time
```

4. Click: `Add Trainer`
5. Trainer is now registered in system

### STEP 2: ASSIGN TRAINER TO MEMBER

**When Adding New Member:**

1. Fill member form (see above)
2. In form, find: `Assign Trainer` dropdown
3. Select: Trainer name (e.g., "Sarah Johnson - Strength Training")
4. Click: `Add Member`
✅ Trainer assigned!

**When Editing Existing Member:**

1. Go to: Members → Click `Edit`
2. Find: `Assign Trainer` dropdown
3. Select: Trainer (or change to different trainer)
4. Click: `Update Member`
✅ Trainer updated!

**View Trainer Workload:**

1. Click: `Trainers`
2. See trainer cards showing:
   - Name
   - Specialization
   - Contact
   - Shift Time
   - **Number of Members** assigned

---

## 📅 ATTENDANCE TRACKING

### RECORD DAILY ATTENDANCE

**Step-by-Step:**

1. **Go to**: Members → Click `View` on member
2. **Click**: `Attendance` tab
3. **Click**: `+ Record Attendance`
4. **Fill form**:

```
📋 ATTENDANCE FORM
├─ Date *                   → Attendance date (e.g., 2026-02-14)
├─ Status *                 → Choose one:
│  ├─ Present  ✅           (Member came to gym)
│  ├─ Absent   ❌           (Member didn't come)
│  └─ Leave    ⏸️           (Member on planned leave)
```

5. **Click**: `Record Attendance`

### VIEW ATTENDANCE HISTORY

1. **Go to**: Member Profile
2. **Click**: `Attendance` tab
3. **See**:
   - All attendance records listed
   - Most recent first
   - Status shown with color codes
     - ✅ Green for Present
     - ❌ Red for Absent
     - 🔵 Blue for Leave

**Example Attendance History:**
```
Date       │ Status   │ Color
2026-02-14 │ Present  │ ✅ Green
2026-02-13 │ Present  │ ✅ Green
2026-02-12 │ Absent   │ ❌ Red
2026-02-11 │ Leave    │ 🔵 Blue
2026-02-10 │ Present  │ ✅ Green
```

---

## 💰 PAYMENT MANAGEMENT

### HOW PAYMENT SYSTEM WORKS

✅ **Automatic Notification Generation**
- When payment recorded → auto notification sent to member
- Payment Paid → "Payment received" notification
- Payment Pending → "Payment due" reminder

### RECORD PAYMENT

**Step-by-Step:**

1. **Go to**: Members → Click `View` on member
2. **Click**: `Payments` tab
3. **Click**: `+ Add Payment`
4. **Fill form**:

```
📋 PAYMENT FORM
├─ Payment Date *           → Date of payment (e.g., 2026-02-14)
├─ Amount ($) *             → Amount paid (e.g., 99.99)
├─ Payment Status *         → Choose one:
│  ├─ Paid                  (Payment received)
│  ├─ Pending               (Waiting for payment)
│  └─ Failed                (Payment failed)
├─ Notes (Optional)         → e.g., "Monthly subscription"
```

5. **Click**: `Record Payment`

### AUTOMATIC NOTIFICATIONS

**What Happens Automatically:**

When you record payment:
```
If Status = "Paid"
└─→ Notification: "Payment of $99.99 received. Thank you!"

If Status = "Pending"
└─→ Notification: "Payment of $99.99 is pending. Please pay by 2026-02-14"

If Status = "Failed"
└─→ Notification: "Payment of $99.99 failed. Please try again."
```

### VIEW PAYMENT HISTORY

1. **Go to**: Member Profile
2. **Click**: `Payments` tab
3. **See**:
   - All payments listed
   - Most recent first
   - Status with color codes
     - ✅ Green for Paid
     - ⚠️ Yellow for Pending
     - ❌ Red for Failed

**Example Payment History:**
```
Date       │ Amount │ Status   │ Color
2026-02-14 │ $99.99 │ Paid     │ ✅
2026-01-14 │ $99.99 │ Paid     │ ✅
2026-12-14 │ $99.99 │ Pending  │ ⚠️
2026-11-14 │ $99.99 │ Paid     │ ✅
```

### VIEW REVENUE ON DASHBOARD

1. **Go to**: Dashboard (click logo or home)
2. **See**: `Total Revenue` card
3. Shows: Sum of all "Paid" payments
4. Example: $2,400.50 (all members' paid fees)

---

## 📅 WORKOUT SCHEDULE & DIET PLANS

### ADD WORKOUT PLAN

**Step-by-Step:**

1. Click: `Workout Plans` in menu
2. Click: `+ Add New Plan`
3. Fill form:

```
📋 WORKOUT PLAN FORM
├─ Fitness Goal *           → Weight Loss / Muscle Gain / Endurance / etc.
├─ Duration *               → 8 weeks / 12 weeks / 16 weeks
├─ Description *            → Detailed plan
│  Example:
│  "4 days per week, 1 hour each
│   Monday: Chest & Triceps (3x8, 3x10, 3x12 reps)
│   Wednesday: Back & Biceps (3x8, 3x10, 3x12 reps)
│   Friday: Legs (4x6, 4x8, 4x10 reps)
│   Saturday: Core (3x15 minutes)"
```

4. Click: `Create Plan`

### ADD DIET PLAN TO MEMBER

**Step-by-Step:**

1. **Go to**: Members → Click `View`
2. **Click**: `Diet Plan` tab
3. **Click**: `+ Add Diet Plan`
4. **Fill form**:

```
📋 DIET PLAN FORM
├─ Diet Goal *              → Weight Loss / Muscle Gain / Maintenance
├─ Meal Type *              → Breakfast / Lunch / Dinner / Snack
├─ Food Items *             → List items
│  Example for Breakfast:
│  "Oatmeal, 2 Eggs, Whole wheat toast, Orange juice, Almonds"
│  
│  Example for Lunch:
│  "Grilled chicken breast, Brown rice, Broccoli, Olive oil"
│  
│  Example for Dinner:
│  "Fish, Sweet potato, Mixed vegetables, Olive oil"
```

5. Click: `Add Diet Plan`

### VIEW DIET PLANS

1. **Go to**: Member Profile
2. **Click**: `Diet Plan` tab
3. **See**: All meal plans in cards
   - Breakfast plan
   - Lunch plan
   - Dinner plan
   - Snack plan

---

## 📋 COMPLETE WORKFLOW EXAMPLE

### SCENARIO: New Member John Joins Gym

**Day 1: Member Registration**

```
STEP 1: Create Trainer (if not exists)
├─ Click: Trainers → + Add New Trainer
├─ Name: Sarah Johnson
├─ Specialization: Strength Training
├─ Shift: 6 AM - 12 PM
└─ Click: Add Trainer ✅

STEP 2: Add Member
├─ Click: Members → + Add New Member
├─ Name: John Doe
├─ DOB: 1995-05-15
├─ Gender: Male
├─ Contact: 9876543210
├─ Weight: 80 kg
├─ Height: 175 cm
├─ Goal: Weight Loss
├─ Join Date: 2026-02-14
├─ Trainer: Sarah Johnson
├─ Click: Add Member
└─ John gets Member ID #1 automatically ✅

STEP 3: Record First Attendance
├─ Click: Members → View John
├─ Attendance Tab
├─ + Record Attendance
├─ Status: Present
├─ Click: Record ✅

STEP 4: Record Payment
├─ Click: Payments Tab
├─ + Add Payment
├─ Amount: $99.99
├─ Status: Paid
├─ Click: Record Payment
└─ Auto-notification sent ✅

STEP 5: Add Diet Plan
├─ Click: Diet Plan Tab
├─ + Add Diet Plan
├─ Meal: Breakfast
├─ Items: "Oatmeal, Eggs, Toast"
├─ Click: Add Diet Plan ✅
```

**Day 7: Track Progress**

```
STEP 1: Record Weight
├─ Click: Members → View John
├─ Progress Tab
├─ + Add Progress
├─ Weight: 78.5 kg (lost 1.5 kg!)
├─ Click: Record Progress
└─ BMI auto-updated ✅

STEP 2: View Dashboard
├─ Click: Dashboard
├─ See: Member count, trainer count, revenue
├─ See: Total revenue includes John's payment
└─ See: John in recent members list ✅
```

---

## ✨ KEY FEATURES SUMMARY

| Feature | How It Works |
|---------|------------|
| **Member ID** | Auto-generated when member is added (1, 2, 3...) |
| **BMI** | Auto-calculated from weight & height |
| **Attendance** | Mark as Present/Absent/Leave daily |
| **Payments** | Track with status, auto-notifications |
| **Weight** | Record regularly, system tracks changes |
| **Trainer** | Assign during registration or edit later |
| **Diet Plan** | Create separate plans for each meal type |
| **Workout** | Create templates, assign to members |
| **Notifications** | Auto-generated for payment status |
| **Dashboard** | Real-time statistics |

---

## 🎯 COMMON TASKS - QUICK REFERENCE

### I want to...

**Add a new member:**
→ Members → + Add New Member → Fill form → Click Add Member

**Track member weight:**
→ Members → View Member → Progress Tab → + Add Progress → Record

**Check attendance:**
→ Members → View Member → Attendance Tab (see all records)

**Mark attendance:**
→ Members → View Member → Attendance Tab → + Record Attendance

**Record payment:**
→ Members → View Member → Payments Tab → + Add Payment

**See member payment history:**
→ Members → View Member → Payments Tab (see all payments)

**Create trainer:**
→ Trainers → + Add New Trainer → Fill → Add Trainer

**Assign trainer to member:**
→ Members → Add Member (choose trainer) OR Edit Member (select different trainer)

**Add diet plan:**
→ Members → View Member → Diet Plan Tab → + Add Diet Plan

**Create workout plan:**
→ Workout Plans → + Add New Plan → Fill → Create Plan

**Check dashboard stats:**
→ Click Dashboard (see total members, trainers, revenue)

---

## 💡 TIPS & TRICKS

✅ **Tip 1**: Member ID is auto-generated (don't create manually)
✅ **Tip 2**: BMI updates automatically when you record progress
✅ **Tip 3**: Trainers must be created before assigning to members
✅ **Tip 4**: Payments auto-create notifications (saves time!)
✅ **Tip 5**: Check dashboard monthly for revenue tracking
✅ **Tip 6**: Edit member details anytime to update trainer
✅ **Tip 7**: Add multiple diet plans per member (one for each meal)
✅ **Tip 8**: View member profile has all info in one place (tabs organize everything)

---

## 🔍 EXAMPLE DATA

### Sample Member Entry
```
Member ID:        #1 (auto-generated)
Name:             John Doe
Date of Birth:    1995-05-15 (Age: 31)
Gender:           Male
Contact:          9876543210
Weight:           80 kg
Height:           175 cm
BMI:              26.12 (auto-calculated)
Goal:             Weight Loss
Join Date:        2026-02-14
Health Issues:    None
Trainer:          Sarah Johnson (Strength Training)
```

### Sample Attendance Record
```
Date:             2026-02-14
Status:           Present ✅
Member:           John Doe (ID #1)
```

### Sample Payment Record
```
Date:             2026-02-14
Amount:           $99.99
Status:           Paid ✅
Member:           John Doe (ID #1)
Note:             Monthly subscription
Auto-Sent:        "Payment received. Thank you!"
```

### Sample Diet Plan
```
Member:           John Doe (ID #1)
Meal Type:        Breakfast
Goal:             Weight Loss
Items:            "Oatmeal, 2 Eggs, Whole Wheat Toast, Orange Juice"
Created:          2026-02-14
```

### Sample Progress Entry
```
Member:           John Doe (ID #1)
Date:             2026-02-21 (1 week later)
Weight:           78.5 kg
BMI:              25.65 (improved!)
Notes:            "Lost 1.5kg, feeling great!"
```

---

## ❓ FREQUENTLY ASKED QUESTIONS

**Q: How is member ID assigned?**
A: Automatically! First member gets ID 1, second gets ID 2, etc.

**Q: How is BMI calculated?**
A: Automatically from weight (kg) ÷ (height in meters)²

**Q: Can I change a member's trainer?**
A: Yes! Go to Members → Edit Member → Select different trainer

**Q: Do notifications happen automatically?**
A: Yes! When you record payment, notification auto-created

**Q: Can I track weight changes?**
A: Yes! Go to Progress tab, it shows all previous weights

**Q: How many payments can a member have?**
A: Unlimited! One per transaction

**Q: Can I edit member details after creation?**
A: Yes! Click Edit in members list

**Q: How do I see trainer workload?**
A: Go to Trainers, see member count on each trainer card

---

**Now you're ready to use the Gym Management System! 💪**

For more help, check the other documentation files.

