# Architecture of Sadeem AI Skills

## الفكرة الأساسية

نريد بناء نظام بسيط جدًا يوضح كيف يمكن أن يعمل أي Agent ذكي من منظور معماري.

الأساس هو أن الـUser يرسل طلبًا، والـAgent يمرره إلى سجل المهارات، ثم يتم اختيار Skill مناسب، ثم يستخدم Tool أو خدمة خارجية، ثم يعيد النتيجة إلى المستخدم.

## العلاقة بين المكونات

### 1. User
المستخدم يكتب أمرًا مثل:

```text
/echo hello
```

أو:

```text
/summarize Python is great
```

### 2. Agent
الـAgent هو نقطة التفاعل الأولى. 
هو الذي يستقبل الرسالة، يقرأ اسم المهارة، ويطلب من الـRegistry الحصول عليها.

### 3. Skill Registry
هذا السجل يحافظ على جميع المهارات المثبتة في التطبيق.

دوره:

- تسجيل Skill
- جلب Skill حسب الاسم
- إرجاع قائمة المهارات المتاحة

### 4. Skill
Skill هو تنفيذ مفهوم محدد، مثل:

- `echo`
- `summarize`

كل Skill يعرف كيف ينجز مهمة ما.

### 5. Tool
Tool هو المكوّن الذي يستخدمه الـSkill للتنفيذ الفعلي.

في هذا المشروع:

- `normalize_text()` يقوم بتنظيف النص
- Gemini API هي Tool خارجية تُستدعى من Skill `summarize`

### 6. Gemini
Gemini هو مزود خارجي للذكاء الاصطناعي. 
نستخدمه في `summarize` فقط لتلخيص النص.

## المخطط العام

```text
User
 ↓
Agent
 ↓
Skill Registry
 ↓
Skill
 ↓
Tool / External API
 ↓
Result
```

## مثال تنفيذ /echo

```text
User: /echo hello
       ↓
Agent: receives input
       ↓
Skill Registry: get("echo")
       ↓
EchoSkill.execute("hello")
       ↓
Result: "hello"
       ↓
User sees: hello
```

## مثال تنفيذ /summarize

```text
User: /summarize Python is a programming language
       ↓
Agent: receives input
       ↓
Skill Registry: get("summarize")
       ↓
SummarizeSkill.execute(text)
       ↓
Tool: Gemini API
       ↓
Result: summarized text
       ↓
User sees summary
```

## لماذا هذه البنية مهمة؟

لأنها تجعل النظام:

- منظمًا
- قابلًا للتوسعة
- أكثر وضوحًا في التعليم
- سهل لفهم العلاقة بين كل مكوّن

## ملاحظة تعليمية

في هذه المرحلة، لا يوجد LLM لاختيار المهارة تلقائيًا.

بدلًا من ذلك، الـAgent يوزع الطلب بطريقة بسيطة جدًا:

- إذا بدأ الأمر بـ `/echo` → EchoSkill
- إذا بدأ الأمر بـ `/summarize` → SummarizeSkill

هذا يركز على البنية المعمارية بدل التعقيد.
