# V1

## Memories

Types:

```python
from evermemos.types.v1 import (
    MemoryType,
    Metadata,
    MemoryCreateResponse,
    MemoryDeleteResponse,
    MemoryGetResponse,
    MemoryLoadResponse,
    MemorySearchResponse,
)
```

Methods:

- <code title="post /api/v1/memories">client.v1.memories.<a href="./src/evermemos/resources/v1/memories/memories.py">create</a>(\*\*<a href="src/evermemos/types/v1/memory_create_params.py">params</a>) -> <a href="./src/evermemos/types/v1/memory_create_response.py">MemoryCreateResponse</a></code>
- <code title="delete /api/v1/memories">client.v1.memories.<a href="./src/evermemos/resources/v1/memories/memories.py">delete</a>(\*\*<a href="src/evermemos/types/v1/memory_delete_params.py">params</a>) -> <a href="./src/evermemos/types/v1/memory_delete_response.py">MemoryDeleteResponse</a></code>
- <code title="get /api/v1/memories">client.v1.memories.<a href="./src/evermemos/resources/v1/memories/memories.py">get</a>() -> <a href="./src/evermemos/types/v1/memory_get_response.py">MemoryGetResponse</a></code>
- <code title="post /api/v1/memories/import">client.v1.memories.<a href="./src/evermemos/resources/v1/memories/memories.py">load</a>(\*\*<a href="src/evermemos/types/v1/memory_load_params.py">params</a>) -> <a href="./src/evermemos/types/v1/memory_load_response.py">MemoryLoadResponse</a></code>
- <code title="get /api/v1/memories/search">client.v1.memories.<a href="./src/evermemos/resources/v1/memories/memories.py">search</a>() -> <a href="./src/evermemos/types/v1/memory_search_response.py">MemorySearchResponse</a></code>

### ConversationMeta

Types:

```python
from evermemos.types.v1.memories import (
    ConversationMetaCreateResponse,
    ConversationMetaUpdateResponse,
    ConversationMetaGetResponse,
)
```

Methods:

- <code title="post /api/v1/memories/conversation-meta">client.v1.memories.conversation_meta.<a href="./src/evermemos/resources/v1/memories/conversation_meta.py">create</a>(\*\*<a href="src/evermemos/types/v1/memories/conversation_meta_create_params.py">params</a>) -> <a href="./src/evermemos/types/v1/memories/conversation_meta_create_response.py">ConversationMetaCreateResponse</a></code>
- <code title="patch /api/v1/memories/conversation-meta">client.v1.memories.conversation_meta.<a href="./src/evermemos/resources/v1/memories/conversation_meta.py">update</a>(\*\*<a href="src/evermemos/types/v1/memories/conversation_meta_update_params.py">params</a>) -> <a href="./src/evermemos/types/v1/memories/conversation_meta_update_response.py">ConversationMetaUpdateResponse</a></code>
- <code title="get /api/v1/memories/conversation-meta">client.v1.memories.conversation_meta.<a href="./src/evermemos/resources/v1/memories/conversation_meta.py">get</a>() -> <a href="./src/evermemos/types/v1/memories/conversation_meta_get_response.py">ConversationMetaGetResponse</a></code>

## Stats

### Request

Types:

```python
from evermemos.types.v1.stats import RequestGetResponse
```

Methods:

- <code title="get /api/v1/stats/request">client.v1.stats.request.<a href="./src/evermemos/resources/v1/stats/request.py">get</a>(\*\*<a href="src/evermemos/types/v1/stats/request_get_params.py">params</a>) -> <a href="./src/evermemos/types/v1/stats/request_get_response.py">RequestGetResponse</a></code>
