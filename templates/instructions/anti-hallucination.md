**CRITICAL**: Follow these rules to prevent invented architecture:

1. **Never speculate** about existing patterns you haven't read

   - ❌ BAD: "The app probably follows a services pattern"
   - ✅ GOOD: "Let me search for existing service files"

2. **Cite existing code** when recommending reuse

   - Example: "Use UserService at api/app/services/user.py:20-45"

3. **Admit when exploration needed**

   - "I need to read package.json and search for imports"

4. **Quote spec.md exactly** - don't paraphrase requirements

5. **Verify dependencies exist** before recommending
   - Check package.json before suggesting libraries

**Why**: Hallucinated architecture leads to 40-50% implementation rework.
