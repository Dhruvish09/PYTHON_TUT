"""
1. Convert "john doe" so only the first letter is capitalized → "John doe".
2. Normalize email addresses: "TEST@EMAIL.COM" → "test@email.com".
3. Convert all strings to uppercase before comparing roles: "admin" vs "ADMIN".
4. Convert book title "the great gatsby" to title case.
5. Convert "Hello World" to "hELLO wORLD" for mock UI toggle.
6. Compare "straße" and "STRASSE" in a Unicode-aware way.

7. Get domain from "user@example.com" using index of "@".
8. Extract "pdf" from "report.final.pdf" using last ".".
9. Ensure "key=value" contains "=" and raise error if not.
10.Get patch version from "version=1.0.5" using last ".".
11.Ensure CSV string has exactly 2 commas.
12.Detect logs starting with "ERROR".
13.Filter filenames ending in ".csv".

14. Replace < and > in HTML tags with &lt; and &gt;.
15. Clean "  password123  " before storing.
16. Clean left-padded number like "   0042".
17. Remove trailing slash from "example.com/path/".
18. Remove "api_" from "api_token".
19. Remove "Controller" from "UserController".

20. Validate username "user123" (letters and numbers only).
21. Check "US" is alphabetic.
22. Check if "2025" is a valid year.
23. Ensure "1234" is decimal (not superscript).
24. Validate Unicode numerals like "Ⅳ".
25. Check password contains lowercase letters.
26. Confirm "SAVE50" is uppercase.
27. Check if "John Smith" is title case.
28. Detect blank lines in text.
29. Check if "foo_bar" is a valid variable.
30. Ensure config strings have only printable chars.

31. Join tags ["fastapi", "python", "api"] → "fastapi,python,api".
32. Split "John,Doe,28" into ['John', 'Doe', '28'].
33. From "backup_2024_06_20.zip", get base before last "_".
34. Split "line1\\nline2\\nline3" into separate lines.
35. Split "mode=production" into ("mode", "=", "production").
36. Split "path/to/file.txt" into ("path/to", "/", "file.txt").

37. Center-align "Header" in a 20-char wide string.
38. Left-align "Key" and pad with dots.
39. Right-align number "42" padded with spaces.
40. Format invoice numbers as "00042".

41. Use format to greet a user → "Hello, Alice!".
42. Format string with dict → "User: Alice, Age: 25".
"""