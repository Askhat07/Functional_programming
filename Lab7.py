def remove_spaces(text):
    return text.replace(" ", "")


def to_lower_case(text):
    return text.lower()


def remove_punctuation(text):
    punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    for char in punctuation:
        text = text.replace(char, "")
    return text


def compose(*functions):
    def composed_function(arg):
        result = arg
        for func in functions:
            result = func(result)
        return result

    return composed_function


composed_operations = compose(remove_spaces, to_lower_case, remove_punctuation)
text = input()
result = composed_operations(text)
print(result)

import asyncio

async def remove_spaces(text):
    await asyncio.sleep(1)
    return text.replace(" ", "")

async def to_lower_case(text):
    await asyncio.sleep(1)
    return text.lower()

async def remove_punctuation_async(text):
    punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    for char in punctuation:
        text = text.replace(char, "")
        await asyncio.sleep(0)
    return text
async def compose(*functions):
    async def composed_function(arg):
        result = arg
        for func in functions:
            result = await func(result)
        return result
    return composed_function



async def main():
    composed_operations = await compose(remove_spaces, to_lower_case, remove_punctuation_async)
    text = input()
    result = await composed_operations(text)
    print(result)
asyncio.run(main())