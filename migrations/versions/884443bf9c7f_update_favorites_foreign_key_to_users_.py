"""update favorites foreign key to users.user_id

Revision ID: 884443bf9c7f
Revises: a68ee5986ac1
Create Date: 2026-01-13 19:56:08.980905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '884443bf9c7f'
down_revision = 'a68ee5986ac1'
branch_labels = None
depends_on = None



def upgrade():
    # users tablosunda id -> user_id rename
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('id', new_column_name='user_id')

    # favorites tablosunda foreign key'i güncelle
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint('favorites_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(
            None, 'users', ['user_id'], ['user_id']
        )

def downgrade():
    # geri dönüş için user_id -> id rename
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('user_id', new_column_name='id')

    # favorites foreign key'i geri al
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(
            'favorites_user_id_fkey', 'users', ['user_id'], ['id']
        )

