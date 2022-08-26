from flask import Blueprint, render_template

# the 'dashboard' is the url_prefix
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# this route is /dashboard
@bp.route('/')
def dash():
  return render_template('dashboard.html')

# this route is /dashboard/edit/<id>
@bp.route('/edit/<id>')
def edit(id):
  return render_template('edit-post.html')