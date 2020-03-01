"""add page model

Revision ID: 6d2cdd0601cf
Revises: 8d32dac5d61e
Create Date: 2020-03-01 20:02:15.682625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d2cdd0601cf'
down_revision = '8d32dac5d61e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pagename', sa.String(length=32), nullable=True),
    sa.Column('file_path', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pages_pagename'), 'pages', ['pagename'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pages_pagename'), table_name='pages')
    op.drop_table('pages')
    # ### end Alembic commands ###
