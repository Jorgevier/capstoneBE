"""updated followers

Revision ID: 77055c80b2d2
Revises: 14e64f17bb79
Create Date: 2024-02-07 19:01:03.651366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77055c80b2d2'
down_revision = '14e64f17bb79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('following',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['resturant.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('following')
    # ### end Alembic commands ###
