from fastapi import FastAPI
import uvicorn




def reserve_str(s:str):
    return {"word": s, "word_servese": s[::-1]}

def to_upper(s:str):
    return {"word": s, "s_upper": s.upper()}

def remove_vowels(s: str):
    pass

def remove_every_third(s:str) -> tuple[str, list[int], list[int]]:
    pass

def letter_count_map(s: str) -> dict[str, int]:
    pass