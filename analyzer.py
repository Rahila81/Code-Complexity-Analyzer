import re


def analyze_code(code):

    lines = code.splitlines()

    # -----------------------------
    # Basic line statistics
    # -----------------------------

    total_lines = len(lines)

    code_lines = 0
    comment_lines = 0

    for line in lines:

        stripped = line.strip()

        if stripped == "":
            continue

        if stripped.startswith("//") or stripped.startswith("#"):
            comment_lines += 1
        else:
            code_lines += 1

    # -----------------------------
    # Count loops
    # -----------------------------

    loop_matches = re.findall(
        r"\b(for|while)\b",
        code
    )

    loop_count = len(loop_matches)

    # -----------------------------
    # Detect nested loops
    # -----------------------------

    max_loop_depth = 0
    current_depth = 0

    for line in lines:

        stripped = line.strip()

        if re.search(r"\b(for|while)\b", stripped):
            current_depth += 1

            if current_depth > max_loop_depth:
                max_loop_depth = current_depth

        if "}" in stripped and current_depth > 0:
            current_depth -= stripped.count("}")

    # -----------------------------
    # Count conditions
    # -----------------------------

    condition_matches = re.findall(
        r"\b(if|else\s+if|else|switch|case)\b",
        code
    )

    condition_count = len(condition_matches)

    # -----------------------------
    # Count functions / methods
    # -----------------------------

    function_matches = re.findall(
        r"\b(def\s+\w+|public\s+\w+\s+\w+\s*\(|private\s+\w+\s+\w+\s*\(|static\s+\w+\s+\w+\s*\()",
        code
    )

    function_count = len(function_matches)

    # -----------------------------
    # Time complexity
    # -----------------------------

    if max_loop_depth == 0:
        time_complexity = "O(1)"
        explanation = "No loops were detected. The code appears to perform constant-time operations."

    elif max_loop_depth == 1:
        time_complexity = "O(n)"
        explanation = "A single loop was detected. Runtime may grow linearly with the input size."

    elif max_loop_depth == 2:
        time_complexity = "O(n²)"
        explanation = "Nested loops were detected. Runtime may grow quadratically with the input size."

    elif max_loop_depth == 3:
        time_complexity = "O(n³)"
        explanation = "Three levels of nested loops were detected. Runtime may grow cubically."

    else:
        time_complexity = f"O(n^{max_loop_depth})"
        explanation = f"{max_loop_depth} levels of nested loops were detected."

    # -----------------------------
    # Space complexity
    # -----------------------------

    array_matches = re.findall(
        r"\b(int|float|double|char|String)\s*\[\]",
        code
    )

    if array_matches:
        space_complexity = "O(n)"
    else:
        space_complexity = "O(1)"

    # -----------------------------
    # Quality score
    # -----------------------------

    score = 100

    if comment_lines == 0 and code_lines > 5:
        score -= 10

    if condition_count > 5:
        score -= 10

    if max_loop_depth >= 3:
        score -= 15

    if code_lines > 100:
        score -= 10

    if score < 0:
        score = 0

    # -----------------------------
    # Return results
    # -----------------------------

    return {
    "total_lines": total_lines,
    "code_lines": code_lines,
    "comments": comment_lines,
    "loops": loop_count,
    "nested_depth": max_loop_depth,
    "conditions": condition_count,
    "functions": function_count,
    "time": time_complexity,
    "space": space_complexity,
    "score": score,
    "explanation": explanation
}