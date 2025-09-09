"""initial

Revision ID: 001
Revises: 
Create Date: 2025-09-09 05:45:23.967285

"""
from alembic import op
import sqlalchemy as sa

revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'space_objects',
        sa.Column('id', sa.String(length=50), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('type', sa.String(length=20), nullable=False),
        sa.Column('tle_line1', sa.String(length=100), nullable=False),
        sa.Column('tle_line2', sa.String(length=100), nullable=False),
        sa.Column('last_update', sa.DateTime(), nullable=False),
    )

    op.create_table(
        'risk_assessments',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('object_id', sa.String(length=50), sa.ForeignKey('space_objects.id')),
        sa.Column('collision_probability', sa.Float(), nullable=False),
        sa.Column('time_to_closest_approach', sa.Float(), nullable=False),
        sa.Column('minimum_distance', sa.Float(), nullable=False),
        sa.Column('assessment_time', sa.DateTime(), nullable=False),
    )

def downgrade():
    op.drop_table('risk_assessments')
    op.drop_table('space_objects')
