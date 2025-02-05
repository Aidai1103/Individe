"""Add grade field to student model

Revision ID: 3e746642fe7f
Revises: b4260c799945
Create Date: 2025-01-28 22:17:12.989651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e746642fe7f'
down_revision = 'b4260c799945'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('IT',
               existing_type=sa.FLOAT(),
               nullable=False)
        batch_op.alter_column('Korean',
               existing_type=sa.FLOAT(),
               nullable=False)
        batch_op.alter_column('grade',
               existing_type=sa.FLOAT(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('grade',
               existing_type=sa.FLOAT(),
               nullable=True)
        batch_op.alter_column('Korean',
               existing_type=sa.FLOAT(),
               nullable=True)
        batch_op.alter_column('IT',
               existing_type=sa.FLOAT(),
               nullable=True)

    # ### end Alembic commands ###
