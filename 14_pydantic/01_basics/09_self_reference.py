from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Comment(BaseModel):
    id : int
    content: str
    replies : Optional[list['Comment']] = None

Comment.model_rebuild()

comment_1 = Comment(id=1, content='This is a comment', replies=[])
comment_2 = Comment(id=2, content='This is a reply to comment 1', replies=[])

comment_1.replies.append(comment_2)

print(comment_1)

comment = Comment(
    id = 3,
    content = 'This is a comment with a nested reply',
    replies = [Comment(id=4, content='This is a reply to comment 3', replies=[
        Comment(id=5, content='This is a nested reply to comment 4', replies=[])])]
    
)

print(comment)