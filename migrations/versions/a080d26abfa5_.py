"""empty message

Revision ID: a080d26abfa5
Revises: 2bc42f9cea51
Create Date: 2021-11-29 00:24:13.745215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a080d26abfa5'
down_revision = '2bc42f9cea51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('resumes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('recruitment', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('resume_name', sa.String(length=256), nullable=True),
    sa.Column('resume_path', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('resumes', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_resumes_recruitment'), ['recruitment'], unique=False)
        batch_op.create_index(batch_op.f('ix_resumes_status'), ['status'], unique=False)
        batch_op.create_index(batch_op.f('ix_resumes_student_id'), ['student_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    with op.batch_alter_table('resumes', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_resumes_student_id'))
        batch_op.drop_index(batch_op.f('ix_resumes_status'))
        batch_op.drop_index(batch_op.f('ix_resumes_recruitment'))

    op.drop_table('resumes')
    # ### end Alembic commands ###