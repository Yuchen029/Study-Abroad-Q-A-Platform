"""empty message

Revision ID: 42022eeb3fae
Revises: 464b8331c7f2
Create Date: 2021-11-28 15:35:50.545890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42022eeb3fae'
down_revision = '464b8331c7f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('college_id', sa.Integer(), nullable=True))
        batch_op.drop_index('ix_users_collage_id')
        batch_op.create_index(batch_op.f('ix_users_college_id'), ['college_id'], unique=True)
        batch_op.drop_column('collage_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('collage_id', sa.INTEGER(), nullable=True))
        batch_op.drop_index(batch_op.f('ix_users_college_id'))
        batch_op.create_index('ix_users_collage_id', ['collage_id'], unique=False)
        batch_op.drop_column('college_id')

    # ### end Alembic commands ###
