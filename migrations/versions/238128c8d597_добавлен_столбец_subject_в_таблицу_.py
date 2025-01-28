"""Добавлен столбец subject в таблицу student

Revision ID: 238128c8d597
Revises: 3bc59032e797
Create Date: 2025-01-28 20:57:12.780359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '238128c8d597'
down_revision = '3bc59032e797'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('subject', sa.String(length=80), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_column('subject')

    # ### end Alembic commands ###
