# Psychological Healthcare Knowledge Base
# Source 1: Clinical Q&A documents (based on NHS.uk and Mind.org.uk public information)
# Source 2: Real counselling conversations loaded from HuggingFace dataset
# Total: 50 documents

# Clinical Q&A Documents (25) 

clinical_docs = []

clinical_docs.append(
    "Q: What is anxiety and what are the symptoms? "
    "A: Anxiety is a feeling of worry, nervousness or unease that can range from mild to severe. "
    "Common symptoms include racing heart, sweating, trouble sleeping, difficulty concentrating, "
    "and avoiding situations that cause worry. "
    "Types include generalised anxiety disorder GAD, panic disorder, social anxiety, and phobias. "
    "If anxiety is affecting your daily life speak to your GP or self-refer to NHS Talking Therapies. "
    "In a crisis call Samaritans on 116 123 free and available 24 hours."
)

clinical_docs.append(
    "Q: What is depression and how is it different from just feeling sad? "
    "A: Depression is more than feeling sad for a few days. It is a persistent low mood that affects "
    "how you think, feel and function over weeks or months. "
    "Symptoms include continuous low mood, loss of interest in activities, low energy, changes in sleep "
    "or appetite, difficulty concentrating, and in severe cases thoughts of self-harm or suicide. "
    "Depression is a medical condition not a sign of weakness. See your GP if symptoms last more than two weeks. "
    "Effective treatments include CBT therapy, antidepressants, exercise, and social support."
)

clinical_docs.append(
    "Q: What is CBT and how does it work? "
    "A: Cognitive Behavioural Therapy CBT is the most widely used evidence-based psychological therapy. "
    "It is based on the idea that our thoughts, feelings and behaviours are interconnected. "
    "Negative thought patterns can maintain and worsen mental health problems. "
    "CBT helps you identify and challenge unhelpful thoughts and change problematic behaviours. "
    "Core techniques include thought records, behavioural activation, and exposure therapy. "
    "CBT is effective for anxiety, depression, OCD, PTSD, and many other conditions. "
    "Access it free through NHS Talking Therapies by self-referring online without needing a GP."
)

clinical_docs.append(
    "Q: How do I access free therapy on the NHS? "
    "A: NHS Talking Therapies previously known as IAPT offers free psychological therapies for anxiety and depression. "
    "You do not need a GP referral. You can self-refer directly by searching NHS Talking Therapies online. "
    "Therapies available include CBT, counselling, guided self-help, and group therapy. "
    "Sessions are delivered by telephone, video, online, or face to face. "
    "Waiting times vary by area. If you need urgent support contact your GP or call NHS 111. "
    "The service is suitable for depression, anxiety, panic, phobias, OCD, PTSD, and stress."
)

clinical_docs.append(
    "Q: What is mindfulness and does it actually help mental health? "
    "A: Mindfulness means paying attention to the present moment intentionally and without judgment. "
    "It has a strong evidence base for reducing anxiety, depression, and stress. "
    "NICE recommends mindfulness-based cognitive therapy MBCT for preventing depression relapse. "
    "Simple practices include focusing on your breath for five minutes, body scan meditation, "
    "and the five senses exercise noticing what you see hear feel smell and taste. "
    "Free resources include the NHS mindfulness course online and apps like Headspace and Calm. "
    "Even five to ten minutes of daily practice makes a difference over time."
)

clinical_docs.append(
    "Q: What are the signs of a panic attack and what should I do during one? "
    "A: A panic attack is a sudden intense episode of fear that causes physical symptoms including "
    "racing heart, shortness of breath, chest tightness, dizziness, shaking, and feeling of losing control. "
    "Panic attacks are frightening but not dangerous. They usually peak within ten minutes and pass. "
    "During a panic attack stay where you are if safe, breathe slowly and deeply, "
    "and use the five four three two one grounding technique naming things you can see hear and feel. "
    "Recurring panic attacks may indicate panic disorder. CBT is the most effective treatment. "
    "See your GP if panic attacks are frequent or affecting your daily life."
)

clinical_docs.append(
    "Q: What is PTSD and what causes it? "
    "A: Post-Traumatic Stress Disorder PTSD can develop after experiencing or witnessing a traumatic event "
    "such as assault, accident, war, disaster, or childhood abuse. "
    "Symptoms include flashbacks and nightmares reliving the event, avoiding reminders of the trauma, "
    "feeling emotionally numb, hypervigilance being constantly on alert, and sleep problems. "
    "PTSD can develop immediately after trauma or months or years later. "
    "Effective treatments include Trauma-Focused CBT and EMDR Eye Movement Desensitisation and Reprocessing "
    "which are recommended first-line treatments by NICE. Recovery is possible with the right support."
)

clinical_docs.append(
    "Q: What is OCD and how is it treated? "
    "A: Obsessive Compulsive Disorder OCD involves unwanted intrusive thoughts called obsessions "
    "and repetitive behaviours called compulsions carried out to reduce the anxiety they cause. "
    "Common obsessions include fear of contamination, fear of harming others, and need for symmetry. "
    "Common compulsions include excessive handwashing, checking locks repeatedly, and counting. "
    "OCD is not about being overly clean or organised. It can be very distressing and time-consuming. "
    "The most effective treatment is Exposure and Response Prevention ERP a form of CBT. "
    "SSRIs medication can also help. See your GP for referral to specialist OCD services."
)

clinical_docs.append(
    "Q: What is bipolar disorder and how is it managed? "
    "A: Bipolar disorder involves episodes of extreme mood changes including manic episodes "
    "of elevated mood high energy and reduced need for sleep, and depressive episodes of low mood. "
    "During manic episodes a person may feel elated or irritable, have racing thoughts, "
    "talk fast, behave recklessly, and have grandiose beliefs. "
    "Bipolar disorder is a long-term condition requiring ongoing management. "
    "Treatment includes mood stabilising medication such as lithium, psychological therapies, "
    "and lifestyle management particularly maintaining a regular sleep routine. "
    "See your GP urgently if you think you may be having a manic episode."
)

clinical_docs.append(
    "Q: What medications are used for anxiety and depression? "
    "A: SSRIs Selective Serotonin Reuptake Inhibitors are the most commonly prescribed medication "
    "for both depression and anxiety. Examples include sertraline, fluoxetine, and citalopram. "
    "They usually take four to six weeks to take full effect. "
    "Common initial side effects include nausea and headaches which usually improve. "
    "Do not stop SSRIs suddenly as this can cause withdrawal effects. Always discuss stopping with your GP. "
    "Mental health medications work best when combined with therapy and lifestyle changes. "
    "Always take medication as prescribed and discuss any concerns with your GP or psychiatrist."
)

clinical_docs.append(
    "Q: How does exercise help mental health? "
    "A: Exercise is one of the most powerful interventions for mental health with strong scientific evidence. "
    "Regular exercise reduces symptoms of depression and anxiety as effectively as medication in some studies. "
    "NICE recommends exercise as a first-line treatment for mild to moderate depression. "
    "Exercise releases endorphins and serotonin, reduces stress hormones, improves sleep quality, "
    "increases self-esteem, and provides social connection in group activities. "
    "Adults need at least 150 minutes of moderate activity per week such as brisk walking or cycling. "
    "Even ten minute walks help. Your GP can refer you to a local exercise programme on prescription."
)

clinical_docs.append(
    "Q: How does sleep affect mental health? "
    "A: Sleep and mental health are closely connected. Poor sleep worsens anxiety and depression "
    "while mental health problems often cause sleep difficulties creating a difficult cycle. "
    "Good sleep hygiene includes going to bed and waking at the same time every day, "
    "avoiding screens for one hour before bed, keeping the bedroom cool dark and quiet, "
    "and avoiding caffeine after 3pm and alcohol before bed. "
    "Cognitive Behavioural Therapy for Insomnia CBT-I is more effective than sleeping pills long-term. "
    "If sleep problems persist for more than four weeks speak to your GP."
)

clinical_docs.append(
    "Q: What is burnout and how do I recover from it? "
    "A: Burnout is a state of physical and emotional exhaustion caused by chronic workplace stress. "
    "Signs include exhaustion that sleep does not fix, cynicism and detachment from work, "
    "reduced performance, and physical symptoms like headaches and frequent illness. "
    "Under the Health and Safety at Work Act employers have a duty to protect mental health. "
    "You can ask for reasonable adjustments if mental health affects your work. "
    "Recovery steps include speaking to your manager or HR, taking sick leave if needed, "
    "and speaking to your GP who can provide support and referrals. "
    "Prevention includes setting clear work-life boundaries and taking all annual leave."
)

clinical_docs.append(
    "Q: How can I help someone with depression? "
    "A: Supporting someone with depression requires patience, empathy, and practical help. "
    "Listen without judgment and avoid telling them to cheer up or snap out of it. "
    "Ask them directly how they are feeling and take what they say seriously. "
    "Help with practical tasks like shopping or cooking if they are struggling to manage. "
    "Encourage them to seek professional help and offer to go with them to a GP appointment. "
    "Stay connected with regular contact even if they withdraw. "
    "Look after your own wellbeing too as supporting someone with depression can be emotionally draining. "
    "If you are worried they may harm themselves call 999 or Samaritans on 116 123."
)

clinical_docs.append(
    "Q: What is self-harm and where can I get help? "
    "A: Self-harm means deliberately hurting yourself as a way of coping with emotional pain or distress. "
    "It is more common than many people realise particularly among young people. "
    "Self-harm is not attention-seeking. It is usually a way of expressing pain that feels impossible to put into words. "
    "If you self-harm you deserve help and support not judgment. "
    "Speak to your GP who can refer you to appropriate services. "
    "Crisis support is available from Samaritans on 116 123 or by texting SHOUT to 85258. "
    "MIND helpline is available on 0300 123 3393. Recovery is possible with the right support."
)

clinical_docs.append(
    "Q: What are the mental health crisis helpline numbers in the UK? "
    "A: Samaritans: call 116 123 free and available 24 hours seven days a week, confidential emotional support. "
    "Shout Crisis Text Line: text SHOUT to 85258 free and available 24 hours. "
    "CALM Campaign Against Living Miserably: 0800 58 58 58 available 5pm to midnight. "
    "PAPYRUS for young people at risk of suicide: 0800 068 4141. "
    "Mind Infoline: 0300 123 3393 Monday to Friday 9am to 6pm. "
    "NHS 111: call 111 and select the mental health option available 24 hours. "
    "In immediate danger always call 999 or go to your nearest Accident and Emergency department."
)

clinical_docs.append(
    "Q: What is social anxiety and how is it treated? "
    "A: Social anxiety is an intense and persistent fear of social situations where you may be "
    "judged, embarrassed, or humiliated by others. It is more than just shyness. "
    "Symptoms include fear of speaking in public, avoiding social situations, intense self-consciousness, "
    "blushing, sweating, and shaking in social contexts. "
    "Social anxiety can significantly affect work, relationships, and daily functioning. "
    "The most effective treatment is CBT specifically exposure therapy gradually facing feared social situations. "
    "Medication such as SSRIs can also help. Self-refer to NHS Talking Therapies for free CBT."
)

clinical_docs.append(
    "Q: How does alcohol affect mental health? "
    "A: Alcohol is a depressant that affects brain chemistry and mental health significantly. "
    "Many people drink to cope with stress or low mood but alcohol makes these problems worse over time. "
    "Short-term effects include low mood, increased anxiety, poor sleep, and impulsive decisions. "
    "Long-term heavy drinking significantly increases risk of depression, anxiety disorders, and psychosis. "
    "Recommended limits are no more than 14 units per week spread over several days with alcohol-free days. "
    "If you drink to manage mental health symptoms this is a warning sign worth discussing with your GP. "
    "Drinkline is available on 0300 123 1110 for support with alcohol concerns."
)

clinical_docs.append(
    "Q: What is grief and how do I cope with loss? "
    "A: Grief is a natural response to loss including the death of a loved one, relationship breakdown, "
    "job loss, or diagnosis of serious illness. There is no right or wrong way to grieve. "
    "You may experience shock, sadness, anger, guilt, anxiety, or even relief at different times. "
    "Most people find grief becomes less intense over time with support and self-care. "
    "Complicated grief that severely impacts daily life after several months may benefit from professional support. "
    "Cruse Bereavement Support is available on 0808 808 1677 free of charge. "
    "Your GP can refer you to bereavement counselling. Talking to others who have experienced similar loss can help."
)

clinical_docs.append(
    "Q: What is the difference between a psychiatrist and a psychologist? "
    "A: A psychiatrist is a medical doctor who specialises in mental health. "
    "They can diagnose mental health conditions, prescribe medication, and provide therapy. "
    "They are involved in more complex or severe mental health cases. "
    "A psychologist has a doctorate in psychology but is not a medical doctor. "
    "They cannot prescribe medication but provide assessment and psychological therapies like CBT. "
    "A counsellor provides talking support and guidance for emotional difficulties. "
    "Your GP is usually your first point of contact who can then refer you to the appropriate professional "
    "depending on the nature and severity of your mental health concerns."
)

clinical_docs.append(
    "Q: What are eating disorders and where can I get help? "
    "A: Eating disorders are serious mental health conditions affecting how people relate to food and their body. "
    "Types include anorexia nervosa restricting food severely, bulimia nervosa cycles of bingeing and purging, "
    "and binge eating disorder. "
    "Warning signs include preoccupation with weight and calories, avoiding eating with others, "
    "and significant weight changes. "
    "Eating disorders have the highest mortality rate of any mental health condition. "
    "Early treatment significantly improves outcomes. "
    "Beat helpline is available on 0808 801 0677. Your GP can refer you to specialist eating disorder services. "
    "NHS Talking Therapies offers CBT for some eating disorders."
)

clinical_docs.append(
    "Q: How do I manage stress effectively? "
    "A: Stress is the body's response to pressure and while some stress is normal, chronic stress harms health. "
    "Effective stress management strategies include regular physical exercise which reduces stress hormones, "
    "good sleep routine, time management and prioritising tasks, "
    "talking to someone you trust, and reducing alcohol and caffeine. "
    "Mindfulness-based stress reduction MBSR has strong evidence for managing chronic stress. "
    "Setting clear boundaries at work and in personal life is essential. "
    "If stress is unmanageable speak to your GP or self-refer to NHS Talking Therapies. "
    "Identifying and addressing the root causes of stress is more effective than managing symptoms alone."
)

clinical_docs.append(
    "Q: What is Mindfulness-Based Cognitive Therapy MBCT? "
    "A: Mindfulness-Based Cognitive Therapy MBCT combines mindfulness practices with cognitive therapy techniques. "
    "It was specifically developed to prevent relapse in people who have experienced repeated episodes of depression. "
    "NICE recommends MBCT for people who have had three or more episodes of depression. "
    "The programme typically runs over eight weeks in a group format. "
    "It teaches participants to become aware of and relate differently to their thoughts, feelings, and body sensations. "
    "Rather than trying to change negative thoughts MBCT teaches people to observe them without judgment. "
    "Ask your GP for a referral or search for MBCT programmes through NHS Talking Therapies."
)

clinical_docs.append(
    "Q: What regulations govern AI systems used in mental health support? "
    "A: The EU AI Act 2024 classifies AI systems used in mental health support as high-risk applications. "
    "This requires mandatory human oversight, rigorous bias testing, transparent documentation, "
    "and clear disclosure to users that they are interacting with an AI system. "
    "Under GDPR mental health data is classified as special category data under Article 9 "
    "requiring explicit user consent, strict security measures, and the right to erasure. "
    "Organisations deploying mental health AI must conduct regular safety audits "
    "and ensure human professional involvement for serious clinical cases. "
    "AI systems should extend access to support not replace human clinical judgment and empathy."
)

clinical_docs.append(
    "Q: What digital tools and apps can help with mental health? "
    "A: Several NHS recommended digital tools can support mental health alongside professional care. "
    "Headspace and Calm offer guided mindfulness and sleep meditations with free trials available. "
    "SilverCloud is an online CBT programme available through NHS Talking Therapies. "
    "Daylio is a mood tracking app that helps identify patterns in mood and behaviour. "
    "Every Mind Matters on the NHS website offers free personalised mental health advice. "
    "Limitations of digital tools include being unsuitable for severe mental health conditions "
    "and inability to replace human connection or professional assessment. "
    "Always check if an app is NHS approved. In a crisis do not rely on an app but contact 999 or Samaritans."
)

print(f"Clinical documents loaded: {len(clinical_docs)}")