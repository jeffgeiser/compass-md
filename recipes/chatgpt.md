# Recipe: ChatGPT

**Storage assumed: No direct storage access.** ChatGPT cannot read Drive or local files automatically. Compass files must be manually uploaded or pasted. This recipe covers how to work with that constraint.

Connect ChatGPT to your compass-md context. ChatGPT's file access model is different from the other recipes — it doesn't have a persistent file connector in the same way Cowork and Claude.ai do — so the patterns here involve more manual setup.

> **Is a prompt alone enough?**
> A prompt gives ChatGPT instructions but no access to your Compass files — it will follow the workflow but read from its training knowledge rather than your actual files. For real file access you need to upload your Compass files to a Custom GPT's Knowledge section (Option 1 below). For quick use without file access, paste a condensed Compass summary into ChatGPT's Custom Instructions (Option 2) — this persists across all conversations but is a compressed approximation. Pasting a prompt in chat with files attached works for one conversation.

Two options, depending on how you use ChatGPT.

---

## Option 1: Custom GPT with Compass files (best experience)

If you use ChatGPT Plus or higher, you can create a Custom GPT with your Compass files uploaded as knowledge. The GPT will reference those files in every conversation.

### Setup

1. **Prepare your Compass files for upload.** Export or download your Compass files. You can upload the full set or a curated subset (voice.md, preferences.md, facts.md, and your main perspective files are usually enough to start).

2. **Create a Custom GPT:**
   - ChatGPT → Explore GPTs → Create a GPT
   - In "Configure," set a name like "My Compass" and a description
   
3. **Upload your Compass files** in the "Knowledge" section. Upload each file separately or zip the folder.

4. **Add Compass instructions** to the system prompt:

   ```
   You have access to the user's Compass — a set of markdown files capturing
   their voice, perspectives, preferences, facts, and decisions. These files
   follow the compass-md convention v0.1.
   
   Before responding to any request:
   1. Review COMPASS.md for this Compass's conventions (uploaded)
   2. Identify which Compass files are relevant:
      - Drafting content → voice.md + relevant perspective files
      - Recommendations → preferences.md + relevant perspectives
      - Context about the user → facts.md
      - Prior decisions → decisions.md
   3. Respond with that context informing your output
   4. Briefly note which Compass files informed the response
   
   If you observe something that warrants a Compass refinement, include a
   "Proposed Compass update" section at the end of your response with:
   - Target file
   - Proposed addition or change
   - Reasoning (1-2 sentences)
   
   Don't claim to have updated the Compass — you can't write files. The user
   will apply accepted proposals manually.
   ```

5. **Test:** Ask the Custom GPT to draft something that should engage your Compass — an email, a recommendation, a decision. Check that it cites Compass files in its response.

### Keeping files current

Uploaded knowledge files don't sync automatically. When you update your Compass (accept a refinement, edit a file directly), re-upload the changed files. This is friction — consider updating the uploaded files on a monthly cadence rather than after every change.

---

## Option 2: Custom instructions (lightweight, less setup)

If you don't want to create a Custom GPT, you can paste condensed Compass content directly into ChatGPT's Custom Instructions. This is less complete but easier to set up and maintain.

### Setup

1. **ChatGPT → Settings → Custom Instructions**

2. In "What would you like ChatGPT to know about you?" paste a condensed summary of your Compass:

   ```
   [Paste a 300-500 word summary of your voice, key preferences, role/context,
   and most important perspectives. This isn't the full Compass — it's a
   compressed version that fits in the custom instructions field.]
   ```

3. In "How would you like ChatGPT to respond?" paste:

   ```
   Use the context in the "About me" section to inform all responses. When
   drafting content on my behalf, use my described voice and preferences.
   When you observe something that should update my context, flag it at the
   end of your response as a suggested update (I'll apply it manually).
   ```

This approach loses the file structure and specificity of a full Compass, but it gives you basic context persistence without Custom GPT setup.

---

## What to expect

Custom GPT with file uploads is the closer analog to the Cowork and Claude.ai experiences. It won't read Drive directly, but it reads your exported files.

Refinements proposed by ChatGPT come back as text in the conversation — you manually update your Compass files. There's no automated write-back.

ChatGPT's Drive connector capabilities are evolving. If OpenAI ships a Drive integration that reads files directly, update this recipe accordingly.

---

## Limitations

No direct Drive access (as of v0.1). Files must be manually uploaded.

Knowledge files in Custom GPTs don't auto-sync. Plan for periodic re-uploads.

The custom instructions character limit (around 1,500 characters per field) makes Option 2 a compressed approximation of your Compass, not the full thing.

Custom GPTs require ChatGPT Plus or higher.
