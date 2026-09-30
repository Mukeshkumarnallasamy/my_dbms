# 🏋️ Gym Management System

A complete web-based gym management system built with Python Flask and SQLite. Manage members, trainers, workout plans, diet plans, payments, attendance, and progress tracking all in one place.

## ✨ Features

### Core Functionalities:
- **Member Management**: Add, edit, view, and delete gym members with complete profiles
- **Trainer Management**: Manage trainers with specialization and shift information
- **Workout Plans**: Create and manage customized workout plans for different fitness goals
- **Diet Plans**: Track meal plans and nutritional information for members
- **Progress Tracking**: Record weight, BMI, and other fitness metrics over time
- **Attendance Tracking**: Mark and monitor member attendance
- **Payment Management**: Record and track membership payments with status
- **Notifications**: Automatic notifications for payment updates
- **Admin Dashboard**: View key metrics and recent activities

### Technical Features:
✅ Secure admin authentication
✅ Database persistence with SQLite
✅ Responsive design (works on desktop and mobile)
✅ Flash messages for user feedback
✅ Professional and clean UI
✅ Easy data management with forms

## 📋 Project Structure

```
GymManagementSystem/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── gym_management.db               # SQLite database (auto-created)
├── templates/                      # HTML templates
│   ├── base.html                  # Base template with navigation
│   ├── login.html                 # Login page
│   ├── dashboard.html             # Admin dashboard
│   ├── members_list.html          # Members list
│   ├── add_member.html            # Add member form
│   ├── edit_member.html           # Edit member form
│   ├── view_member.html           # Member details
│   ├── trainers_list.html         # Trainers list
│   ├── add_trainer.html           # Add trainer form
│   ├── edit_trainer.html          # Edit trainer form
│   ├── add_progress.html          # Record progress form
│   ├── add_attendance.html        # Record attendance form
│   ├── add_payment.html           # Record payment form
│   ├── add_diet.html              # Add diet plan form
│   ├── workout_plans_list.html    # Workout plans list
│   ├── add_workout_plan.html      # Add workout plan form
│   └── 404.html                   # 404 error page
└── static/
    └── css/
        └── style.css              # Main stylesheet
```

## 🗄️ Database Schema

### Main Entities:

1. **Admin** - System administrators
2. **Member** - Gym members (central entity)
3. **Trainer** - Fitness trainers
4. **Workout_Plan** - Exercise plans
5. **Diet** - Nutritional plans
6. **Progress** - Fitness tracking
7. **Attendance** - Attendance records
8. **Payment** - Payment information
9. **Notification** - System notifications

## 🚀 Getting Started

### Prerequisites:
- Python 3.7+
- pip (Python package manager)
- Windows/Mac/Linux

### Installation Steps:

1. **Navigate to project directory**:
   ```bash
   cd GymManagementSystem
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open in browser**:
   - Navigate to `http://localhost:5000`
   - You will be redirected to the login page

### Default Credentials:
- **Username**: `admin`
- **Password**: `admin123`

**⚠️ Important**: Change these credentials in production!

## 📖 How to Use

### 1. Login
- Use the default credentials or create a new admin account
- Demo credentials provided on login page

### 2. Dashboard
- View key metrics (total members, trainers, revenue)
- See recent member join dates
- Quick access to add new members/trainers/plans

### 3. Members Management
- **Add Member**: Click "+ Add New Member" and fill required information
- **View Member**: Click "View" to see complete member profile with all related records
- **Edit Member**: Update member information like weight, height, goal, trainer assignment
- **Delete Member**: Remove member from system (with confirmation)

### 4. Member Details (Comprehensive View)
- **Progress Tab**: Track weight changes and BMI over time
- **Attendance Tab**: View attendance history
- **Payments Tab**: Track payment status and history
- **Diet Tab**: View assigned diet plans

### 5. Trainer Management
- **Add Trainer**: Create new trainer profiles with specialization
- **Edit Trainer**: Update trainer information
- **Delete Trainer**: Remove trainers from system
- **View Members**: See how many members are assigned to each trainer

### 6. Workout Plans
- Create customized plans for different fitness goals
- Examples: Weight Loss, Muscle Gain, Endurance, Flexibility, Strength

### 7. Recording Information
- **Progress**: Record weight and BMI measurements
- **Attendance**: Mark members as Present/Absent/Leave
- **Payments**: Record membership fees with status tracking
- **Diet Plans**: Create meal plans for members (Breakfast/Lunch/Dinner/Snack)

## 🎯 Key Features in Detail

### Member Profile
- Personal information (name, DOB, gender, contact)
- Physical measurements (weight, height, BMI calculation)
- Fitness goal and health issues
- Trainer assignment
- Complete history of progress, attendance, payments, and diet

### Progress Tracking
- Automatic BMI calculation
- Date-based tracking
- Notes for each progress entry
- Visual history of member improvements

### Payment System
- Track payment status (Paid/Pending/Failed)
- Automatic notifications generation
- Member payment history
- Revenue tracking on dashboard

### Attendance Management
- Simple check-in system
- Status options (Present/Absent/Leave)
- Historical attendance records
- Easy attendance marking

## 🎨 UI/UX Features

- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Modern Styling**: Clean, professional interface with gradients
- **Intuitive Navigation**: Easy-to-use menu system
- **Color-Coded Badges**: Visual status indicators for payments and attendance
- **Flash Messages**: Clear feedback for user actions
- **Tabbed Interface**: Organized information display for member details
- **Data Tables**: Easy-to-scan information in tabular format
- **Card-Based Layout**: Modern card design for better visual hierarchy

## 💾 Database

- **Type**: SQLite3 (file-based)
- **Location**: `gym_management.db` (auto-created)
- **No setup required**: Database tables created automatically on first run
- **Default admin**: Created automatically if no admin exists

## 🔐 Security Features

- Password hashing for admin accounts (werkzeug.security)
- Session-based authentication
- Login required for all management pages
- CSRF protection recommended for production

## 📝 Notes

### For Production Deployment:
1. Change the secret key in `app.py`:
   ```python
   app.config['SECRET_KEY'] = 'your-secure-key-here'
   ```

2. Set `debug=False` in the last line:
   ```python
   app.run(debug=False)
   ```

3. Use a production WSGI server (Gunicorn, uWSGI)

4. Set up proper database backups

5. Use HTTPS for secure connections

## 🐛 Troubleshooting

### Issue: Port 5000 already in use
**Solution**: 
```bash
# Use a different port
python -c "from app import app; app.run(port=5001)"
```

### Issue: Database locked error
**Solution**: 
- Restart the application
- Delete `gym_management.db` (fresh start)

### Issue: Module not found
**Solution**:
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

## 🚀 Future Enhancements

- Email notifications for payments and reminders
- Member mobile app
- Advanced analytics and reports
- Trainer-specific dashboard
- Member self-service portal
- Integration with payment gateways
- Backup and restore functionality
- Export data to PDF/Excel

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Ensure Python version is 3.7+
4. Check that port 5000 is available

## 📄 License

This project is provided as-is for educational purposes.

## 🎓 Learning Goals

This mini-project demonstrates:
- Flask web framework basics
- SQLAlchemy ORM
- Database relationships (1-to-M, M-to-M)
- User authentication
- CRUD operations
- Form handling
- HTML/CSS responsive design
- Session management
- Error handling

---

**Happy coding! 💪 Keep fit and manage your gym efficiently!**
