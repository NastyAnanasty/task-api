from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=500)


class Source(BaseModel):
    url: str
    snippet: str = Field(..., description="First ~200 chars of the chunk")
    full_context: str = Field("", description="Full chunk text — for programmatic consumers of the REST API, not shown in UI")


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]