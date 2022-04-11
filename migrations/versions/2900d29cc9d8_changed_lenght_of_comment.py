"""changed lenght of comment

Revision ID: 2900d29cc9d8
Revises: 40b862c8b218
Create Date: 2022-04-11 13:32:12.690454

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2900d29cc9d8'
down_revision = '40b862c8b218'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('campaignname', table_name='campaign')
    op.drop_table('campaign')
    op.create_foreign_key(None, 'comment', 'post', ['post_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'comment', 'user', ['author'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'like', 'post', ['post_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'like', 'user', ['author'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'post', 'user', ['author'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_constraint(None, 'like', type_='foreignkey')
    op.drop_constraint(None, 'like', type_='foreignkey')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.create_table('campaign',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('campaignname', mysql.VARCHAR(length=150), nullable=True),
    sa.Column('date_created', mysql.DATETIME(), nullable=True),
    sa.Column('customquestion1', mysql.VARCHAR(length=150), nullable=True),
    sa.Column('customquestion2', mysql.VARCHAR(length=150), nullable=True),
    sa.Column('customquestion3', mysql.VARCHAR(length=150), nullable=True),
    sa.Column('author', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='MyISAM'
    )
    op.create_index('campaignname', 'campaign', ['campaignname'], unique=False)
    # ### end Alembic commands ###
