from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gym_management.db'
app.config['SECRET_KEY'] = 'your-secret-key-here'
db = SQLAlchemy(app)

# ==================== DATABASE MODELS ====================

class Admin(db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    contact_no = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Trainer(db.Model):
    __tablename__ = 'trainer'
    trainer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    contact_no = db.Column(db.String(15), nullable=False)
    shift_time = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    members = db.relationship('Member', backref='trainer', lazy=True)


class Member(db.Model):
    __tablename__ = 'member'
    member_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    contact_no = db.Column(db.String(15), nullable=False)
    weight = db.Column(db.Float, nullable=False)  # in kg
    height = db.Column(db.Float, nullable=False)  # in cm
    health_issue = db.Column(db.String(250), default="None")
    goal = db.Column(db.String(100), nullable=False)
    join_date = db.Column(db.Date, nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.trainer_id'))
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.admin_id'))
    
    progress = db.relationship('Progress', backref='member', lazy=True, cascade='all, delete-orphan')
    attendance = db.relationship('Attendance', backref='member', lazy=True, cascade='all, delete-orphan')
    payments = db.relationship('Payment', backref='member', lazy=True, cascade='all, delete-orphan')
    notifications = db.relationship('Notification', backref='member', lazy=True, cascade='all, delete-orphan')
    diet = db.relationship('Diet', backref='member', lazy=True, cascade='all, delete-orphan')
    
    def calculate_bmi(self):
        if self.height > 0:
            height_m = self.height / 100
            return round(self.weight / (height_m ** 2), 2)
        return 0


class Workout_Plan(db.Model):
    __tablename__ = 'workout_plan'
    workout_id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    duration = db.Column(db.String(50), nullable=False)  # e.g., "12 weeks"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Diet(db.Model):
    __tablename__ = 'diet'
    diet_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.member_id'), nullable=False)
    goal = db.Column(db.String(100), nullable=False)
    meal_type = db.Column(db.String(50), nullable=False)  # Breakfast, Lunch, Dinner, Snack
    items = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Progress(db.Model):
    __tablename__ = 'progress'
    progress_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.member_id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    notes = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Attendance(db.Model):
    __tablename__ = 'attendance'
    attendance_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.member_id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # Present/Absent/Leave
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Payment(db.Model):
    __tablename__ = 'payment'
    payment_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.member_id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # Paid/Pending/Failed
    notes = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Notification(db.Model):
    __tablename__ = 'notification'
    notif_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.member_id'), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    date = db.Column(db.Date, nullable=False)
    read_status = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class User(db.Model):
    """Model for gym members to login"""
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.member_id'), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    member = db.relationship('Member', backref='user_account')
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)


class TrainerUser(db.Model):
    """Model for trainers to login"""
    __tablename__ = 'trainer_user'
    trainer_user_id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.trainer_id'), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    trainer = db.relationship('Trainer', backref='trainer_account')
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)


class Slot(db.Model):
    """Model for gym class/training slots"""
    __tablename__ = 'slot'
    slot_id = db.Column(db.Integer, primary_key=True)
    slot_name = db.Column(db.String(100), nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.trainer_id'), nullable=False)
    day_of_week = db.Column(db.String(20), nullable=False)  # Monday, Tuesday, etc.
    start_time = db.Column(db.String(10), nullable=False)  # HH:MM format
    end_time = db.Column(db.String(10), nullable=False)
    capacity = db.Column(db.Integer, default=20)
    description = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    trainer = db.relationship('Trainer', backref='slots')
    bookings = db.relationship('Booking', backref='slot', lazy=True, cascade='all, delete-orphan')


class Booking(db.Model):
    """Model for member slot bookings"""
    __tablename__ = 'booking'
    booking_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.member_id'), nullable=False)
    slot_id = db.Column(db.Integer, db.ForeignKey('slot.slot_id'), nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Confirmed')  # Confirmed, Cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    member = db.relationship('Member', backref='bookings')


# ==================== ROUTES ====================

@app.route('/')
def index():
    if 'admin_id' in session:
        return redirect(url_for('admin_dashboard'))
    elif 'member_id' in session:
        return redirect(url_for('member_dashboard'))
    elif 'trainer_id' in session:
        return redirect(url_for('trainer_dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_type = request.form.get('user_type', 'admin')  # admin, member, trainer
        
        if user_type == 'admin':
            admin = Admin.query.filter_by(username=username).first()
            if admin and admin.check_password(password):
                session['admin_id'] = admin.admin_id
                session['admin_name'] = admin.name
                session['user_type'] = 'admin'
                flash(f'Welcome {admin.name}!', 'success')
                return redirect(url_for('admin_dashboard'))
        
        elif user_type == 'member':
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                session['member_id'] = user.member_id
                session['member_name'] = user.member.name
                session['user_type'] = 'member'
                flash(f'Welcome {user.member.name}!', 'success')
                return redirect(url_for('member_dashboard'))
        
        elif user_type == 'trainer':
            trainer_user = TrainerUser.query.filter_by(username=username).first()
            if trainer_user and trainer_user.check_password(password):
                session['trainer_id'] = trainer_user.trainer_id
                session['trainer_name'] = trainer_user.trainer.name
                session['user_type'] = 'trainer'
                flash(f'Welcome {trainer_user.trainer.name}!', 'success')
                return redirect(url_for('trainer_dashboard'))
        
        flash('Invalid username, password, or user type', 'danger')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully', 'info')
    return redirect(url_for('login'))


@app.route('/dashboard')
def admin_dashboard():
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    total_members = Member.query.count()
    total_trainers = Trainer.query.count()
    total_payments = db.session.query(db.func.sum(Payment.amount)).filter_by(status='Paid').scalar() or 0
    recent_members = Member.query.order_by(Member.join_date.desc()).limit(5).all()
    
    return render_template('dashboard.html', 
                         total_members=total_members,
                         total_trainers=total_trainers,
                         total_payments=total_payments,
                         recent_members=recent_members)


@app.route('/member/dashboard')
def member_dashboard():
    if 'member_id' not in session:
        return redirect(url_for('login'))
    
    member = Member.query.get_or_404(session.get('member_id'))
    attendance = Attendance.query.filter_by(member_id=member.member_id).order_by(Attendance.date.desc()).limit(10).all()
    payments = Payment.query.filter_by(member_id=member.member_id).order_by(Payment.payment_date.desc()).limit(5).all()
    diet = Diet.query.filter_by(member_id=member.member_id).all()
    progress = Progress.query.filter_by(member_id=member.member_id).order_by(Progress.date.desc()).limit(5).all()
    notifications = Notification.query.filter_by(member_id=member.member_id).order_by(Notification.date.desc()).limit(5).all()
    now = datetime.now()
    
    return render_template('member_dashboard.html', 
                         member=member,
                         attendance=attendance,
                         payments=payments,
                         diet=diet,
                         progress=progress,
                         notifications=notifications,
                         now=now)


@app.route('/trainer/dashboard')
def trainer_dashboard():
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    trainer = Trainer.query.get_or_404(session.get('trainer_id'))
    members = Member.query.filter_by(trainer_id=trainer.trainer_id).all()
    slots = Slot.query.filter_by(trainer_id=trainer.trainer_id).all()
    recent_attendance = Attendance.query.filter_by(member_id=Member.member_id).order_by(Attendance.date.desc()).limit(10).all()
    
    return render_template('trainer_dashboard.html',
                         trainer=trainer,
                         members=members,
                         slots=slots,
                         recent_attendance=recent_attendance)


# ==================== REGISTRATION ROUTES ====================

@app.route('/register/member', methods=['GET', 'POST'])
def register_member():
    if request.method == 'POST':
        trainers = Trainer.query.all()
        username = request.form.get('username')
        email = request.form.get('email')

        # simple pre-checks to avoid DB unique constraint errors
        if User.query.filter_by(username=username).first():
            flash('Username already taken. Please choose a different one.', 'danger')
            return render_template('register_member.html', trainers=trainers)
        if User.query.filter_by(email=email).first():
            flash('Email already registered. Please use another email or login.', 'danger')
            return render_template('register_member.html', trainers=trainers)

        try:
            # Create Member with default placeholder values
            member = Member(
                name=username,
                dob=datetime.utcnow().date(),
                gender='Not Specified',
                contact_no='',
                weight=0.0,
                height=0.0,
                health_issue='None',
                goal='General Fitness',
                join_date=datetime.utcnow().date(),
                trainer_id=None
            )
            db.session.add(member)
            db.session.flush()  # Get the member_id
            
            # Create User account for login
            user = User(
                member_id=member.member_id,
                username=username,
                email=email
            )
            user.set_password(request.form.get('password'))
            db.session.add(user)
            db.session.commit()
            
            flash('Registration successful! Please login with your credentials.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            # fallback generic error
            flash(f'Error during registration: {str(e)}', 'danger')
    else:
        trainers = Trainer.query.all()
    trainers = Trainer.query.all()
    return render_template('register_member.html', trainers=trainers)


@app.route('/register/trainer', methods=['GET', 'POST'])
def register_trainer():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')

        if TrainerUser.query.filter_by(username=username).first():
            flash('Username already taken. Choose a different one.', 'danger')
            return render_template('register_trainer.html')
        if TrainerUser.query.filter_by(email=email).first():
            flash('Email already registered. Please use another email or login.', 'danger')
            return render_template('register_trainer.html')

        try:
            # Create Trainer first
            trainer = Trainer(
                name=request.form.get('name'),
                specialization=request.form.get('specialization'),
                contact_no=request.form.get('contact_no'),
                email=email,
                shift_time=request.form.get('shift_time')
            )
            db.session.add(trainer)
            db.session.flush()  # Get the trainer_id
            
            # Create TrainerUser account for login
            trainer_user = TrainerUser(
                trainer_id=trainer.trainer_id,
                username=username,
                email=email
            )
            trainer_user.set_password(request.form.get('password'))
            db.session.add(trainer_user)
            db.session.commit()
            
            flash('Trainer registration successful! Please login with your credentials.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error during trainer registration: {str(e)}', 'danger')
    
    return render_template('register_trainer.html')


# ==================== MEMBER ROUTES ====================

@app.route('/members')
def members_list():
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    members = Member.query.all()
    return render_template('members_list.html', members=members, now=datetime.now().date())


@app.route('/member/add', methods=['GET', 'POST'])
def add_member():
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    trainers = Trainer.query.all()
    if request.method == 'POST':
        try:
            member = Member(
                name=request.form.get('name'),
                dob=datetime.strptime(request.form.get('dob'), '%Y-%m-%d').date(),
                gender=request.form.get('gender'),
                contact_no=request.form.get('contact_no'),
                weight=float(request.form.get('weight')),
                height=float(request.form.get('height')),
                health_issue=request.form.get('health_issue'),
                goal=request.form.get('goal'),
                join_date=datetime.strptime(request.form.get('join_date'), '%Y-%m-%d').date(),
                trainer_id=request.form.get('trainer_id') or None,
                admin_id=session.get('admin_id')
            )
            db.session.add(member)
            db.session.commit()
            flash('Member added successfully!', 'success')
            return redirect(url_for('members_list'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('add_member.html', trainers=trainers)


@app.route('/member/<int:member_id>/edit', methods=['GET', 'POST'])
def edit_member(member_id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    member = Member.query.get_or_404(member_id)
    trainers = Trainer.query.all()
    
    if request.method == 'POST':
        try:
            member.name = request.form.get('name')
            member.gender = request.form.get('gender')
            member.contact_no = request.form.get('contact_no')
            member.weight = float(request.form.get('weight'))
            member.height = float(request.form.get('height'))
            member.health_issue = request.form.get('health_issue')
            member.goal = request.form.get('goal')
            member.trainer_id = request.form.get('trainer_id') or None
            
            db.session.commit()
            flash('Member updated successfully!', 'success')
            return redirect(url_for('members_list'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('edit_member.html', member=member, trainers=trainers)


@app.route('/member/<int:member_id>/view')
def view_member(member_id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    member = Member.query.get_or_404(member_id)
    progress = Progress.query.filter_by(member_id=member_id).all()
    attendance = Attendance.query.filter_by(member_id=member_id).all()
    payments = Payment.query.filter_by(member_id=member_id).all()
    diet = Diet.query.filter_by(member_id=member_id).all()
    
    return render_template('view_member.html', member=member, progress=progress, 
                         attendance=attendance, payments=payments, diet=diet)


@app.route('/member/<int:member_id>/delete')
def delete_member(member_id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    member = Member.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()
    flash('Member deleted successfully!', 'danger')
    return redirect(url_for('members_list'))


# ==================== TRAINER ROUTES ====================

@app.route('/trainers')
def trainers_list():
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    trainers = Trainer.query.all()
    return render_template('trainers_list.html', trainers=trainers)


@app.route('/trainer/add', methods=['GET', 'POST'])
def add_trainer():
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            trainer = Trainer(
                name=request.form.get('name'),
                specialization=request.form.get('specialization'),
                contact_no=request.form.get('contact_no'),
                email=request.form.get('email'),
                shift_time=request.form.get('shift_time')
            )
            db.session.add(trainer)
            db.session.commit()
            flash('Trainer added successfully!', 'success')
            return redirect(url_for('trainers_list'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('add_trainer.html')


@app.route('/trainer/<int:trainer_id>/edit', methods=['GET', 'POST'])
def edit_trainer(trainer_id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    trainer = Trainer.query.get_or_404(trainer_id)
    
    if request.method == 'POST':
        try:
            trainer.name = request.form.get('name')
            trainer.specialization = request.form.get('specialization')
            trainer.contact_no = request.form.get('contact_no')
            trainer.email = request.form.get('email')
            trainer.shift_time = request.form.get('shift_time')
            
            db.session.commit()
            flash('Trainer updated successfully!', 'success')
            return redirect(url_for('trainers_list'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('edit_trainer.html', trainer=trainer)


@app.route('/trainer/<int:trainer_id>/delete')
def delete_trainer(trainer_id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    trainer = Trainer.query.get_or_404(trainer_id)
    db.session.delete(trainer)
    db.session.commit()
    flash('Trainer deleted successfully!', 'danger')
    return redirect(url_for('trainers_list'))


# ==================== PROGRESS ROUTES ====================

@app.route('/member/<int:member_id>/progress/add', methods=['GET', 'POST'])
def add_progress(member_id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    member = Member.query.get_or_404(member_id)
    
    if request.method == 'POST':
        try:
            weight = float(request.form.get('weight'))
            bmi = member.calculate_bmi() if weight else 0
            
            progress = Progress(
                member_id=member_id,
                date=datetime.strptime(request.form.get('date'), '%Y-%m-%d').date(),
                weight=weight,
                bmi=bmi,
                notes=request.form.get('notes')
            )
            db.session.add(progress)
            db.session.commit()
            flash('Progress recorded successfully!', 'success')
            return redirect(url_for('view_member', member_id=member_id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('add_progress.html', member=member, now=datetime.now().date())


# ==================== ATTENDANCE ROUTES ====================

@app.route('/member/<int:member_id>/attendance/add', methods=['GET', 'POST'])
def add_attendance(member_id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    member = Member.query.get_or_404(member_id)
    
    if request.method == 'POST':
        try:
            attendance = Attendance(
                member_id=member_id,
                date=datetime.strptime(request.form.get('date'), '%Y-%m-%d').date(),
                status=request.form.get('status')
            )
            db.session.add(attendance)
            db.session.commit()
            flash('Attendance recorded successfully!', 'success')
            return redirect(url_for('view_member', member_id=member_id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('add_attendance.html', member=member)


# ==================== PAYMENT ROUTES ====================

@app.route('/member/<int:member_id>/payment/add', methods=['GET', 'POST'])
def add_payment(member_id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    member = Member.query.get_or_404(member_id)
    
    if request.method == 'POST':
        try:
            payment = Payment(
                member_id=member_id,
                amount=float(request.form.get('amount')),
                payment_date=datetime.strptime(request.form.get('payment_date'), '%Y-%m-%d').date(),
                status=request.form.get('status'),
                notes=request.form.get('notes')
            )
            db.session.add(payment)
            
            # Create notification
            if request.form.get('status') == 'Paid':
                notification = Notification(
                    member_id=member_id,
                    message=f'Payment of ${payment.amount} received. Thank you!',
                    date=datetime.utcnow().date()
                )
            else:
                notification = Notification(
                    member_id=member_id,
                    message=f'Payment of ${payment.amount} is pending. Please pay by {payment.payment_date}',
                    date=datetime.utcnow().date()
                )
            
            db.session.add(notification)
            db.session.commit()
            flash('Payment recorded successfully!', 'success')
            return redirect(url_for('view_member', member_id=member_id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('add_payment.html', member=member)


# ==================== DIET ROUTES ====================

@app.route('/member/<int:member_id>/diet/add', methods=['GET', 'POST'])
def add_diet(member_id):
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    member = Member.query.get_or_404(member_id)
    
    if request.method == 'POST':
        try:
            diet = Diet(
                member_id=member_id,
                goal=request.form.get('goal'),
                meal_type=request.form.get('meal_type'),
                items=request.form.get('items')
            )
            db.session.add(diet)
            db.session.commit()
            flash('Diet plan added successfully!', 'success')
            return redirect(url_for('view_member', member_id=member_id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('add_diet.html', member=member)


# ==================== WORKOUT PLAN ROUTES ====================

@app.route('/workout-plans')
def workout_plans_list():
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    plans = Workout_Plan.query.all()
    return render_template('workout_plans_list.html', plans=plans)


@app.route('/workout-plan/add', methods=['GET', 'POST'])
def add_workout_plan():
    if 'admin_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            plan = Workout_Plan(
                goal=request.form.get('goal'),
                description=request.form.get('description'),
                duration=request.form.get('duration')
            )
            db.session.add(plan)
            db.session.commit()
            flash('Workout plan added successfully!', 'success')
            return redirect(url_for('workout_plans_list'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('add_workout_plan.html')


# ==================== SLOT ROUTES ====================

@app.route('/slots')
def slots_list():
    if 'admin_id' not in session and 'trainer_id' not in session and 'member_id' not in session:
        return redirect(url_for('login'))
    
    slots = Slot.query.all()
    return render_template('slots_list.html', slots=slots)


@app.route('/slot/add', methods=['GET', 'POST'])
def add_slot():
    if 'admin_id' not in session and 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            trainer_id = request.form.get('trainer_id')
            if not trainer_id and 'trainer_id' in session:
                trainer_id = session.get('trainer_id')
            
            slot = Slot(
                slot_name=request.form.get('slot_name'),
                trainer_id=int(trainer_id),
                day_of_week=request.form.get('day_of_week'),
                start_time=request.form.get('start_time'),
                end_time=request.form.get('end_time'),
                capacity=int(request.form.get('capacity', 20)),
                description=request.form.get('description')
            )
            db.session.add(slot)
            db.session.commit()
            flash('Slot added successfully!', 'success')
            return redirect(url_for('slots_list'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    trainers = Trainer.query.all()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render_template('add_slot.html', trainers=trainers, days=days)


@app.route('/slot/<int:slot_id>/edit', methods=['GET', 'POST'])
def edit_slot(slot_id):
    if 'admin_id' not in session and 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    slot = Slot.query.get_or_404(slot_id)
    
    if request.method == 'POST':
        try:
            slot.slot_name = request.form.get('slot_name')
            slot.day_of_week = request.form.get('day_of_week')
            slot.start_time = request.form.get('start_time')
            slot.end_time = request.form.get('end_time')
            slot.capacity = int(request.form.get('capacity', 20))
            slot.description = request.form.get('description')
            
            db.session.commit()
            flash('Slot updated successfully!', 'success')
            return redirect(url_for('slots_list'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render_template('edit_slot.html', slot=slot, days=days)


@app.route('/slot/<int:slot_id>/delete')
def delete_slot(slot_id):
    if 'admin_id' not in session and 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    slot = Slot.query.get_or_404(slot_id)
    db.session.delete(slot)
    db.session.commit()
    flash('Slot deleted successfully!', 'danger')
    return redirect(url_for('slots_list'))


# ==================== BOOKING ROUTES ====================

@app.route('/bookings')
def bookings_list():
    if 'admin_id' not in session and 'member_id' not in session:
        return redirect(url_for('login'))
    
    if 'member_id' in session:
        bookings = Booking.query.filter_by(member_id=session.get('member_id')).all()
    else:
        bookings = Booking.query.all()
    
    return render_template('bookings_list.html', bookings=bookings)


@app.route('/slot/<int:slot_id>/book', methods=['GET', 'POST'])
def book_slot(slot_id):
    if 'member_id' not in session:
        flash('Please login as a member to book a slot', 'warning')
        return redirect(url_for('login'))
    
    slot = Slot.query.get_or_404(slot_id)
    member_id = session.get('member_id')
    
    if request.method == 'POST':
        try:
            # Check if member already booked this slot
            existing_booking = Booking.query.filter_by(
                member_id=member_id,
                slot_id=slot_id
            ).first()
            
            if existing_booking:
                flash('You have already booked this slot!', 'warning')
                return redirect(url_for('slots_list'))
            
            # Check if slot has capacity
            current_bookings = Booking.query.filter_by(slot_id=slot_id, status='Confirmed').count()
            if current_bookings >= slot.capacity:
                flash('Slot is full! Cannot book now.', 'danger')
                return redirect(url_for('slots_list'))
            
            booking = Booking(
                member_id=member_id,
                slot_id=slot_id,
                status='Confirmed'
            )
            db.session.add(booking)
            
            # Create notification
            notification = Notification(
                member_id=member_id,
                message=f'You have successfully booked {slot.slot_name} on {slot.day_of_week}s from {slot.start_time} to {slot.end_time}',
                date=datetime.utcnow().date()
            )
            db.session.add(notification)
            db.session.commit()
            
            flash('Slot booked successfully!', 'success')
            return redirect(url_for('member_dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('confirm_booking.html', slot=slot)


@app.route('/booking/<int:booking_id>/cancel', methods=['POST'])
def cancel_booking(booking_id):
    if 'member_id' not in session:
        return redirect(url_for('login'))
    
    booking = Booking.query.get_or_404(booking_id)
    
    # Check if it's the member's booking
    if booking.member_id != session.get('member_id'):
        if 'admin_id' not in session:
            flash('Unauthorized action', 'danger')
            return redirect(url_for('bookings_list'))
    
    try:
        booking.status = 'Cancelled'
        db.session.commit()
        flash('Booking cancelled successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')
    
    return redirect(url_for('bookings_list') if 'admin_id' in session else url_for('member_dashboard'))


# ==================== TRAINER ATTENDANCE & DIET ROUTES ====================

@app.route('/trainer/attendance/add/<int:member_id>', methods=['GET', 'POST'])
def trainer_add_attendance(member_id):
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    member = Member.query.get_or_404(member_id)
    
    # Check if member is assigned to this trainer
    if member.trainer_id != session.get('trainer_id'):
        flash('Member is not assigned to you', 'danger')
        return redirect(url_for('trainer_dashboard'))
    
    if request.method == 'POST':
        try:
            attendance = Attendance(
                member_id=member_id,
                date=datetime.strptime(request.form.get('date'), '%Y-%m-%d').date(),
                status=request.form.get('status')
            )
            db.session.add(attendance)
            db.session.commit()
            flash('Attendance recorded successfully!', 'success')
            return redirect(url_for('trainer_dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('trainer_add_attendance.html', member=member)


@app.route('/trainer/diet/assign/<int:member_id>', methods=['GET', 'POST'])
def trainer_assign_diet(member_id):
    if 'trainer_id' not in session:
        return redirect(url_for('login'))
    
    member = Member.query.get_or_404(member_id)
    
    # Check if member is assigned to this trainer
    if member.trainer_id != session.get('trainer_id'):
        flash('Member is not assigned to you', 'danger')
        return redirect(url_for('trainer_dashboard'))
    
    if request.method == 'POST':
        try:
            diet = Diet(
                member_id=member_id,
                goal=request.form.get('goal'),
                meal_type=request.form.get('meal_type'),
                items=request.form.get('items')
            )
            db.session.add(diet)
            db.session.commit()
            flash('Diet plan assigned successfully!', 'success')
            return redirect(url_for('trainer_dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('trainer_assign_diet.html', member=member)


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Create default admin if not exists
        if not Admin.query.first():
            admin = Admin(
                name='System Admin',
                username='admin',
                email='admin@gym.com',
                contact_no='9999999999'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("Default admin created: Username: admin, Password: admin123")
    
    app.run(debug=True)
