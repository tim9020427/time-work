from chonkie import SemanticChunker

text = """Artificial intelligence is transforming industries worldwide. 
Machine learning algorithms can now process vast amounts of data efficiently.
Deep learning models have achieved remarkable accuracy in complex tasks.

Climate change poses significant challenges to our planet.
Rising temperatures affect ecosystems and biodiversity globally.
Sustainable practices are essential for environmental preservation.

Quantum computing represents a paradigm shift in computation.
These systems leverage quantum mechanical phenomena for processing.
Potential applications include cryptography and drug discovery."""

text_messy = """Artificial intelligence is transforming industries worldwide. Machine learning algorithms can now process vast amounts of data efficiently. Deep learning models have achieved remarkable accuracy in complex tasks. Climate change poses significant challenges to our planet. Rising temperatures affect ecosystems and biodiversity globally. Sustainable practices are essential for environmental preservation. Quantum computing represents a paradigm shift in computation. These systems leverage quantum mechanical phenomena for processing. Potential applications include cryptography and drug discovery."""

text_zh = '''起点中文网(www.qidian.com)创立于2002年5月，是国内知名的原创文学网站，隶属于阅文集团旗下. 起点中文网以推动中国原创文学事业为宗旨，长期致力于原创文学作者的挖掘与培养，并取得了巨大成果：2003年10月，起点中文网开启“在线收费阅读”服务，成为真正意义上的网络文学赢利模式的先锋之一，就此奠定了原创文学的行业基础. 此后，起点又推出了作家福利、文学交互、内容发掘推广、版权管理等机制和体系，为原创文学的发展注入了巨大活力，有力推动了中国文学原创事业的发展. 在清晨的微光中，一只孤独的猫头鹰在古老的橡树上低声吟唱，它的歌声如同夜色的回声，穿越了时间的迷雾. 树叶在微风中轻轻摇曳，仿佛在诉说着古老的故事，每一个音符都带着森林的秘密. 一位年轻的程序员正专注地敲打着键盘，代码的海洋在他眼前展开. 他的手指在键盘上飞舞，如同钢琴家在演奏一曲复杂的交响乐. 屏幕上的光标闪烁，仿佛在等待着下一个指令，引领他进入未知的数字世界. '''

# Create semantic chunker
chunker = SemanticChunker(
    embedding_model="../potion-multilingual-128M",
    threshold=0.75,  # Higher threshold = more similar content grouped
    chunk_size=1024
)

chunks = chunker.chunk(text_zh)

# Analyze semantic groupings
for i, chunk in enumerate(chunks):
    print(f"\n--- Semantic Group {i+1} ---")
    print(f"Content: {chunk.text[:100]}...")
    print(f"Token count: {chunk.token_count}")
    print(f"Theme: {chunk.text.split('.')[0]}")  # First sentence as theme indicator