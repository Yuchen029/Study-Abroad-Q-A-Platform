"""empty message

Revision ID: 464b8331c7f2
Revises: 2091f422f0d0
Create Date: 2021-11-28 15:03:46.344295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '464b8331c7f2'
down_revision = '2091f422f0d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('collage_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('certification', sa.Integer(), nullable=True))
        batch_op.drop_index('ix_users_student_id')
        batch_op.create_index(batch_op.f('ix_users_certification'), ['certification'], unique=True)
        batch_op.create_index(batch_op.f('ix_users_collage_id'), ['collage_id'], unique=True)
        batch_op.drop_column('student_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('student_id', sa.INTEGER(), nullable=True))
        batch_op.drop_index(batch_op.f('ix_users_collage_id'))
        batch_op.drop_index(batch_op.f('ix_users_certification'))
        batch_op.create_index('ix_users_student_id', ['student_id'], unique=False)
        batch_op.drop_column('certification')
        batch_op.drop_column('collage_id')

    # ### end Alembic commands ###