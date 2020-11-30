"""product table

Revision ID: 72ddddc32f22
Revises: 
Create Date: 2020-11-30 16:22:41.940597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72ddddc32f22'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('instock', sa.Boolean(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('description', sa.String(length=140), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('category')
    # ### end Alembic commands ###
