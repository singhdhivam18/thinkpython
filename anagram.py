def is_angram(first_anagram,second_angram):
    if len(first_anagram)==len(second_angram):
        if sorted(first_anagram)==sorted(second_angram):
            return True
    else:
        return False
ans=is_angram('silent','listen')
print(ans)


