# 2. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать
# знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

text = """Lorem ipsum dolor sit amet. Ut dolores quae 33 harum aperiam qui expedita minima ut sequi nisi qui odit corporis. Aut sint amet sed obcaecati tenetur est similique voluptatem non possimus sint. Non nulla cumque 33 dignissimos quasi id expedita ipsa cum omnis doloremque sit sunt voluptates eos assumenda velit. Sit rerum aliquid et ratione voluptates et eius assumenda id quasi molestias non quaerat culpa.

Quo sunt distinctio non doloremque nostrum qui porro asperiores sed natus rerum sed consequuntur velit. Et excepturi soluta qui Quis rerum sed odit quas eos repellendus doloribus! Eum unde aspernatur ut natus totam ea voluptatum repudiandae est itaque repellat sit blanditiis rerum. Eos voluptas voluptas qui doloribus odio aut facere placeat et recusandae internos qui cupiditate rerum vel asperiores exercitationem quo aliquid velit.

Eum quos recusandae hic doloribus atque quo inventore omnis qui nemo Quis non nihil provident. Ea totam ipsam ut ipsam velit qui veniam aspernatur."""

delete = ".,!?;:-[]{}()='«»—"
for i in delete:
  text: str = text.replace(i, "")

text = text.lower()

print(sorted(set(text.split()), key=lambda x: text.count(x))[-10:])