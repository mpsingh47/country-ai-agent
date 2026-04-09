from typing import TypedDict, List, Dict, Optional

class AgentState(TypedDict):
    query: str
    country: Optional[str]
    fields: List[str]
    data: Dict
    answer: Optional[str]
    error: Optional[str]