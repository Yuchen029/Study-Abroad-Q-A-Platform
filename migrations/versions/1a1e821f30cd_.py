"""empty message

Revision ID: 1a1e821f30cd
Revises: e3cc3e27c422
Create Date: 2021-11-30 17:11:59.677519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a1e821f30cd'
down_revision = 'e3cc3e27c422'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_certifications')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    op.create_table('_alembic_tmp_certifications',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('confirmed', sa.BOOLEAN(), nullable=True),
    sa.Column('teacher_id', sa.INTEGER(), nullable=True),
    sa.Column('certification_name', sa.VARCHAR(length=256), nullable=True),
    sa.Column('certification_path', sa.VARCHAR(length=256), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.CheckConstraint('confirmed IN (0, 1)'),
    sa.CheckConstraint('confirmed IN (0, 1)'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
