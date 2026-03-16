"""Fix favorites foreign key manually

Revision ID: f8dd3449b558
Revises: 74043ace6950
Create Date: 2026-02-10 13:43:43.352346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8dd3449b558'
down_revision = '74043ace6950'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('favorites_game_id_fkey','favorites',type_='foreignkey')
    
    op.create_foreign_key(
        'favorites_game_id_fkey',
        'favorites','games',
        ['game_id'],['game_id']
    )

def downgrade():
    op.drop_constraint('favorites_game_id_fkey','favorites',type_='foreignkey')
    op.create_foreign_key(
        'favorites_game_id_fkey',
        'favorites','games',
        ['game_id'],['id']
    )   
