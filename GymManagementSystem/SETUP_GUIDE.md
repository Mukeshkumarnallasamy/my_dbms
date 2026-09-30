# 📚 Gym Management System - Complete Setup Guide

A step-by-step guide to get the Gym Management System up and running on your computer.

## 🖥️ System Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Python**: Version 3.7 or higher
- **RAM**: Minimum 2GB
- **Disk Space**: Minimum 500MB

## 📥 Installation Guide

### Step 1: Check if Python is Installed

**Windows:**
```bash
python --version
```

**Mac/Linux:**
```bash
python3 --version
```

If you see a version number (e.g., Python 3.9.0), Python is installed. Otherwise, install it from [python.org](https://www.python.org/downloads/)

### Step 2: Download the Project

1. Extract the `GymManagementSystem` folder to your desired location
2. Open Command Prompt (Windows) or Terminal (Mac/Linux)
3. Navigate to the project folder:
   ```bash
   cd path/to/GymManagementSystem
   ```

### Step 3: Quick Start (Easiest Method)

**Windows:**
- Double-click `run.bat` file
- The application will start automatically

**Mac/Linux:**
1. Make the script executable:
   ```bash
   chmod +x run.sh
   ```
2. Run it:
   ```bash
   ./run.sh
   ```

### Step 4: Manual Installation (If Quick Start Doesn't Work)

#### Create Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Run Application
```bash
python app.py
```

### Step 5: Access the Application

1. Open your web browser
2. Go to: `http://localhost:5000`
3. You should see the login page

## 🔐 Login

**Default Credentials:**
- Username: `admin`
- Password: `admin123`

⚠️ **Security Note**: Change these credentials immediately in production!

## 📊 Adding Sample Data (Optional)

To populate the database with sample data for testing:

```bash
python add_sample_data.py
```

This will add:
- 4 sample trainers
- 5 sample members
- 4 workout plans
- Diet plans for each member
- Progress records
- Attendance records
- Payment records

## 🎯 First Steps After Login

1. **Dashboard**: Check the overview and statistics
2. **Add Trainer**: Create a trainer (Menu: Trainers → + Add New Trainer)
3. **Add Member**: Add a member (Menu: Members → + Add New Member)
4. **Create Workout Plan**: Design a workout plan
5. **Record Progress**: Track member improvements

## 📁 File Structure Explained

```
GymManagementSystem/
├── app.py                    # Main application file - all business logic
├── requirements.txt          # Python packages needed
├── README.md                 # Project overview
├── SETUP_GUIDE.md           # This file
├── run.bat                  # Quick start for Windows
├── run.sh                   # Quick start for Mac/Linux
├── add_sample_data.py       # Script to add sample data
├── gym_management.db        # Database (created automatically)
├── templates/               # HTML pages
│   ├── base.html           # Navigation and layout
│   ├── login.html          # Login page
│   ├── dashboard.html      # Main dashboard
│   ├── members_list.html   # Members page
│   ├── add_member.html     # Add member form
│   ├── edit_member.html    # Edit member form
│   ├── view_member.html    # Member details
│   ├── trainers_list.html  # Trainers page
│   ├── add_trainer.html    # Add trainer form
│   ├── edit_trainer.html   # Edit trainer form
│   ├── add_progress.html   # Record progress
│   ├── add_attendance.html # Record attendance
│   ├── add_payment.html    # Record payment
│   ├── add_diet.html       # Add diet plan
│   ├── workout_plans_list.html # Workout plans
│   ├── add_workout_plan.html # Add workout plan
│   └── 404.html            # Error page
└── static/
    └── css/
        └── style.css       # Styling
```

## 🚀 Features Overview

### Member Management
- Create detailed member profiles
- Assign trainers to members
- Track health issues and fitness goals
- Update member information

### Trainer Management
- Register trainers with specialization
- Assign shift times
- View trainer workload
- Manage trainer availability

### Progress Tracking
- Record weight and BMI
- Automatic BMI calculation
- Track improvements over time
- Add personal notes

### Attendance System
- Mark attendance daily
- Track Present/Absent/Leave status
- View attendance history
- Monitor member commitment

### Payment Management
- Record payments with status
- Track payment history
- View revenue
- Automatic notifications

### Diet & Workout Plans
- Create customized meal plans
- Assign workout routines by goal
- Track meal types and items
- Support multiple diet plans per member

## 🔧 Troubleshooting

### Problem: "Python not found"
**Solution**: 
- Install Python from python.org
- Add Python to PATH during installation
- Restart Command Prompt/Terminal after installation

### Problem: "Port 5000 already in use"
**Solution**: 
    ```bash
    # Edit app.py, change last line to:
    app.run(port=5001, debug=True)
    ```

### Problem: "ModuleNotFoundError: No module named 'flask'"
**Solution**: 
    ```bash
    # Reinstall dependencies
    pip install -r requirements.txt
    ```

### Problem: "Database locked"
**Solution**: 
- Restart the application
- Delete `gym_management.db` file (backup first!)
- Application will create new database

### Problem: Losing changes after refresh
**Solution**: This means the database isn't saving. Check:
- Database file permissions
- Available disk space
- Try deleting and recreating database

## 📝 Common Tasks

### Change Admin Password
1. Delete `gym_management.db` file
2. Restart the application
3. New default admin created automatically

### Export Data
1. The database file is `gym_management.db`
2. Backup this file periodically
3. Can be used for data migration

### Increase Database Size
- SQLite supports up to 140TB (more than enough!)
- No additional configuration needed

### Run on Different Port
Edit `app.py` last line:
```python
app.run(port=8000, debug=True)  # Use port 8000
```

## 🔒 Security Tips

1. **Change Default Password**: Modify admin credentials
2. **Use HTTPS**: In production, use SSL certificates
3. **Regular Backups**: Back up `gym_management.db` regularly
4. **Secure Secret Key**: Change in `app.py`
5. **Disable Debug Mode**: Set `debug=False` in production

## 📱 Mobile Access

The application is fully responsive:
- Works on tablets and mobile phones
- Responsive design adapts to all screen sizes
- Touch-friendly interface

To access from other devices on your network:
1. Find your computer's IP address
   ```bash
   ipconfig      # Windows
   ifconfig      # Mac/Linux
   ```
2. Other devices can access: `http://YOUR_IP:5000`

## 🆘 Getting Help

### Common Issues Quick Links

| Issue | Solution |
|-------|----------|
| Installation fails | Check internet connection, verify Python version |
| Can't login | Use: admin / admin123, check caps lock |
| Page not loading | Clear browser cache, try different browser |
| Database error | Delete gym_management.db, restart app |
| Port error | Use port 5001 or 8000 instead |

## 🎓 Learning Resources

### Understanding the Code
- `app.py`: Contains all database models and web routes
- Models section: Database table definitions
- Routes section: Web page handlers
- Forms: HTML templates in templates/ folder

### Customization
- Edit CSS: `static/css/style.css`
- Modify forms: Edit HTML in `templates/` folder
- Change colors: Find `:root` in style.css

## ✅ Verification Checklist

After installation, verify everything works:

- [ ] Application starts without errors
- [ ] Can login with admin/admin123
- [ ] Dashboard displays correctly
- [ ] Can add a trainer
- [ ] Can add a member
- [ ] Can view member details
- [ ] Can record progress
- [ ] Can record attendance
- [ ] Can add payments
- [ ] Database file exists

## 📞 Support Resources

- Python Issues: [python.org](https://www.python.org)
- Flask Documentation: [flask.palletsprojects.com](https://flask.palletsprojects.com)
- SQLite Help: [sqlite.org](https://www.sqlite.org)

---

## 🎉 You're Ready!

Your Gym Management System is ready to use. Start adding trainers, members, and tracking their progress!

**Happy Gym Management! 💪**

---

**Version**: 1.0
**Last Updated**: February 2026
