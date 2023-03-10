"""empty message

Revision ID: b3718c136973
Revises: de544a00327f
Create Date: 2021-11-28 23:23:25.884328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3718c136973'
down_revision = 'de544a00327f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_certification')
        batch_op.create_index(batch_op.f('ix_users_certification'), ['certification'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_certification'))
        batch_op.create_index('ix_users_certification', ['certification'], unique=False)

    # ### end Alembic commands ###
