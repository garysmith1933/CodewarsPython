def golf_score_calculator(par_string, score_string):
    overall_score = 0 
    idx = 0
    
    while idx < len(score_string):
        round_score = int(score_string[idx]) - int(par_string[idx])
        overall_score += round_score
        idx += 1
    
    return overall_score

# Time: O(N) either length of score string or par string
# Space: O(1)