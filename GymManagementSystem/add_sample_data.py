"""
Sample Data Generator for Gym Management System
Run this script to populate the database with sample data for testing
"""

from app import app, db, Admin, Member, Trainer, Workout_Plan, Diet, Progress, Attendance, Payment, Notification
from datetime import datetime, timedelta
import random

def add_sample_data():
    with app.app_context():
        # Clear existing data
        db.session.query(Notification).delete()
        db.session.query(Payment).delete()
        db.session.query(Attendance).delete()
        db.session.query(Progress).delete()
        db.session.query(Diet).delete()
        db.session.query(Member).delete()
        db.session.query(Trainer).delete()
        db.session.query(Workout_Plan).delete()
        
        print("Adding sample trainers...")
        trainers_data = [
            {
                'name': 'John Smith',
                'specialization': 'Strength Training',
                'contact_no': '9876543210',
                'email': 'john@gym.com',
                'shift_time': '6 AM - 12 PM'
            },
            {
                'name': 'Sarah Johnson',
                'specialization': 'Cardio & Endurance',
                'contact_no': '9876543211',
                'email': 'sarah@gym.com',
                'shift_time': '12 PM - 6 PM'
            },
            {
                'name': 'Alex Martinez',
                'specialization': 'Yoga & Flexibility',
                'contact_no': '9876543212',
                'email': 'alex@gym.com',
                'shift_time': '6 PM - 10 PM'
            },
            {
                'name': 'Emily Davis',
                'specialization': 'CrossFit',
                'contact_no': '9876543213',
                'email': 'emily@gym.com',
                'shift_time': 'Full Time'
            }
        ]
        
        trainers = []
        for trainer_data in trainers_data:
            trainer = Trainer(**trainer_data)
            db.session.add(trainer)
            trainers.append(trainer)
        
        db.session.commit()
        print(f"✓ Added {len(trainers)} trainers")
        
        print("Adding sample workout plans...")
        plans_data = [
            {
                'goal': 'Weight Loss',
                'description': 'High-intensity interval training (HIIT) for 30 mins, 5 days a week. Includes cardio, light weights, and core training.',
                'duration': '12 weeks'
            },
            {
                'goal': 'Muscle Gain',
                'description': 'Progressive resistance training with compound exercises. Focus on chest, back, legs. High protein diet recommended.',
                'duration': '16 weeks'
            },
            {
                'goal': 'Endurance',
                'description': 'Running and cycling programs. Start with 30 mins gradually increase to 60 mins. 4 days per week.',
                'duration': '10 weeks'
            },
            {
                'goal': 'Flexibility',
                'description': 'Yoga and stretching routines. 45 mins sessions, 3 times per week. Focus on mobility and balance.',
                'duration': '8 weeks'
            }
        ]
        
        plans = []
        for plan_data in plans_data:
            plan = Workout_Plan(**plan_data)
            db.session.add(plan)
            plans.append(plan)
        
        db.session.commit()
        print(f"✓ Added {len(plans)} workout plans")
        
        print("Adding sample members...")
        members_data = [
            {
                'name': 'Raj Kumar',
                'dob': datetime(1995, 5, 15).date(),
                'gender': 'Male',
                'contact_no': '9111111111',
                'weight': 85.5,
                'height': 175,
                'health_issue': 'None',
                'goal': 'Weight Loss',
                'join_date': datetime.now().date()
            },
            {
                'name': 'Priya Singh',
                'dob': datetime(1998, 8, 22).date(),
                'gender': 'Female',
                'contact_no': '9222222222',
                'weight': 62.0,
                'height': 160,
                'health_issue': 'None',
                'goal': 'Muscle Gain',
                'join_date': (datetime.now() - timedelta(days=30)).date()
            },
            {
                'name': 'Ahmed Hassan',
                'dob': datetime(1988, 3, 10).date(),
                'gender': 'Male',
                'contact_no': '9333333333',
                'weight': 92.0,
                'height': 180,
                'health_issue': 'Mild back pain',
                'goal': 'Endurance',
                'join_date': (datetime.now() - timedelta(days=60)).date()
            },
            {
                'name': 'Lisa Anderson',
                'dob': datetime(2000, 11, 5).date(),
                'gender': 'Female',
                'contact_no': '9444444444',
                'weight': 55.0,
                'height': 165,
                'health_issue': 'None',
                'goal': 'Flexibility',
                'join_date': (datetime.now() - timedelta(days=15)).date()
            },
            {
                'name': 'Vikram Patel',
                'dob': datetime(1992, 7, 20).date(),
                'gender': 'Male',
                'contact_no': '9555555555',
                'weight': 78.5,
                'height': 172,
                'health_issue': 'None',
                'goal': 'Muscle Gain',
                'join_date': (datetime.now() - timedelta(days=45)).date()
            }
        ]
        
        members = []
        admin_id = Admin.query.first().admin_id
        
        for i, member_data in enumerate(members_data):
            member = Member(
                **member_data,
                trainer_id=trainers[i % len(trainers)].trainer_id,
                admin_id=admin_id
            )
            db.session.add(member)
            members.append(member)
        
        db.session.commit()
        print(f"✓ Added {len(members)} members")
        
        print("Adding sample diet plans...")
        diet_count = 0
        for member in members:
            diet_items = [
                {'goal': member.goal, 'meal_type': 'Breakfast', 'items': 'Oatmeal, Eggs, Whole wheat toast, Orange juice'},
                {'goal': member.goal, 'meal_type': 'Lunch', 'items': 'Grilled chicken, Brown rice, Broccoli, Olive oil'},
                {'goal': member.goal, 'meal_type': 'Dinner', 'items': 'Fish/Tofu, Sweet potato, Mixed vegetables'},
                {'goal': member.goal, 'meal_type': 'Snack', 'items': 'Protein shake, Almonds, Banana'}
            ]
            for diet_item in diet_items:
                diet = Diet(member_id=member.member_id, **diet_item)
                db.session.add(diet)
                diet_count += 1
        
        db.session.commit()
        print(f"✓ Added {diet_count} diet plans")
        
        print("Adding sample progress records...")
        progress_count = 0
        for member in members:
            for week in range(0, 12, 2):  # 6 entries over 12 weeks
                progress_date = datetime.now().date() - timedelta(weeks=12-week)
                weight_change = (12-week) * 0.5  # Simulate weight change
                weight = member.weight - (weight_change if member.goal == 'Weight Loss' else -weight_change/2)
                bmi = weight / ((member.height / 100) ** 2)
                
                progress = Progress(
                    member_id=member.member_id,
                    date=progress_date,
                    weight=round(weight, 1),
                    bmi=round(bmi, 2),
                    notes=f'Week {12-week}: Consistent progress. Feeling good!'
                )
                db.session.add(progress)
                progress_count += 1
        
        db.session.commit()
        print(f"✓ Added {progress_count} progress records")
        
        print("Adding sample attendance records...")
        attendance_count = 0
        for member in members:
            for day in range(0, 30, 2):  # 15 entries over 30 days
                att_date = datetime.now().date() - timedelta(days=day)
                status = random.choice(['Present', 'Present', 'Present', 'Absent', 'Leave'])  # 60% present
                
                attendance = Attendance(
                    member_id=member.member_id,
                    date=att_date,
                    status=status
                )
                db.session.add(attendance)
                attendance_count += 1
        
        db.session.commit()
        print(f"✓ Added {attendance_count} attendance records")
        
        print("Adding sample payment records...")
        payment_count = 0
        for member in members:
            for month in range(0, 3):  # 3 months of payments
                pay_date = datetime.now().date() - timedelta(days=30*month)
                status = random.choice(['Paid', 'Paid', 'Pending'])  # 66% paid
                amount = 99.99
                
                payment = Payment(
                    member_id=member.member_id,
                    amount=amount,
                    payment_date=pay_date,
                    status=status,
                    notes='Monthly membership'
                )
                db.session.add(payment)
                
                # Create notification
                if status == 'Paid':
                    message = f'Payment of ${amount} received. Thank you!'
                else:
                    message = f'Payment of ${amount} is pending. Please pay by {pay_date}'
                
                notification = Notification(
                    member_id=member.member_id,
                    message=message,
                    date=pay_date,
                    read_status=month > 0  # Older notifications marked as read
                )
                db.session.add(notification)
                payment_count += 1
        
        db.session.commit()
        print(f"✓ Added {payment_count} payment records")
        
        print("\n" + "="*50)
        print("✓ Sample data added successfully!")
        print("="*50)
        print("\nYou can now login with:")
        print("  Username: admin")
        print("  Password: admin123")
        print("\nSample members have been created with various data.")
        print("Feel free to add more data through the web interface.")

if __name__ == '__main__':
    add_sample_data()
