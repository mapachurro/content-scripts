หากคุณได้ส่งเงินทุนจากบัญชีแลกเปลี่ยน Binance ของคุณไปยัง MetaMask และไม่เห็นเงินทุนเหล่านั้นภายในกระเป๋าเงินของคุณ เราขอแนะนำให้คุณปฏิบัติตามขั้นตอนเหล่านี้:


**ขั้นตอนที่ 1: ตรวจสอบธุรกรรมดังกล่าวบนตัวสำรวจบล็อกเชน**
----------------------------------------------------------


ก่อนอื่นคุณจะต้องตรวจสอบว่า เครือข่ายใดที่ Binance ใช้ในการดำเนินการธุรกรรมดังกล่าวให้เสร็จสมบูรณ์ คุณสามารถทำเช่นนั้นได้โดยการตรวจสอบรายละเอียดการถอนบน Binance:  
![mceclip0.png](https://support.metamask.io/hc/article_attachments/4416068979483/mceclip0.png)


จากนั้นคุณจะต้องไปที่ Explorer ของเครือข่าย นี่คือบางตัวอย่าง:


* [Etherscan](https://etherscan.io/) สำหรับ Ethereum Mainnet
* [Bscscan](https://bscscan.com/) สำหรับ BSC (Binance Smart Chain)
* [Polygonscan](https://polygonscan.com/) สำหรับ Polygon
* [Snowtrace](https://snowtrace.io/) สำหรับ Avalanche


เมื่ออยู่บนตัวสำรวจบล็อกเชนนั้นแล้ว ให้ค้นหาที่อยู่ MetaMask ของคุณหรือค้นหา [รหัสธุรกรรม](https://support.metamask.io/hc/en-us/articles/4413442094235) เพื่อเรียกรายละเอียดของธุรกรรมดังกล่าวขึ้นมาและยืนยันว่ามีการดำเนินการเสร็จสมบูรณ์แล้ว


![mceclip1.png](https://support.metamask.io/hc/article_attachments/4416075037595/mceclip1.png)


ในส่วนภาพรวมของหน้าบัญชีของคุณในตัวสำรวจบล็อก คุณจะสามารถดูยอดคงเหลือโทเค็นของคุณได้ หากโทเค็นดังกล่าวเป็นโทเค็นท้องถิ่น (BNB, ETH, MATIC, AVAX) โทเค็นนั้นจะปรากฏในส่วนยอดคงเหลือ (เช่นในภาพหน้าจอด้านบน)


หากไม่ใช่โทเค็นท้องถิ่นแล้ว โทเค็นนั้นจะปรากฏในเมนูแบบเลื่อนลงในส่วน 'Token' (โทเค็น)


 


**ขั้นตอนที่ 2: เพิ่มเครือข่ายดังกล่าวไปยัง MetaMask และแสดงผลโทเค็นหากจำเป็น**
-------------------------------------------------------------------------------


หากต้องการเพิ่มเครือข่าย โปรดตรวจสอบคู่มือของเราเพื่อเพิ่มโดยใช้ [Chainlist](https://support.metamask.io/hc/en-us/articles/360058992772-Add-a-network-using-Chainlist-Extension-or-Mobile-) หรือ[ดูบทความของเราสำหรับการเพิ่มเครือข่ายแบบกำหนดเอง](https://support.metamask.io/hc/en-us/articles/360043227612-How-to-add-a-custom-network-RPC)


หลังจากเพิ่มเครือข่าย หากโทเค็นของคุณไม่ใช่ Native Token ของเครือข่ายนั้น คุณจะต้อง[แสดงโทเค็นเป็นโทเค็นที่กำหนดเอง](https://support.metamask.io/hc/en-us/articles/360015489031-How-to-add-unlisted-tokens-custom-tokens-in-MetaMask) 


 บนตัวสำรวจบล็อกเชน ให้ไปที่ส่วนโทเค็นและคลิกที่โทเค็นที่คุณได้รับ: 


![mceclip2.png](https://support.metamask.io/hc/article_attachments/4416075047451/mceclip2.png)


 


หากต้องการเพิ่มโทเค็นที่กำหนดไปยัง MetaMask คุณจะต้อง:


1. คัดลอก Contract Address ของโทเค็น โปรดดู[ที่นี่](https://support.metamask.io/hc/en-us/articles/360015488811-What-is-a-Token-Contract-Address-)สำหรับคำแนะนำเพิ่มเติม โดยจำเป็นคุณต้องหาโทเค็นบน Block Explorer และรับที่อยู่จากที่นั่น
2. ไปที่ MetaMask และค้นหา 'Import Tokens' (นำเข้าโทเค็น) ภายใต้แท็บ 'Assets' (สินทรัพย์) คุณอาจต้องเลื่อนหาเล็กน้อยกว่าจะพบโดยจะขึ้นอยู่กับจำนวนโทเค็นที่คุณได้เพิ่มไปแล้ว คลิกที่สิ่งนี้เพื่อเพิ่มโทเค็น ป้อนที่อยู่ของโทเค็น


หากคุณได้ส่งโทเค็นไปผิดเครือข่าย คุณสามารถใช้สะพานเชื่อมเพื่อรับโทเค็นนั้นบนเครือข่ายที่ต้องการได้เสมอ


คุณสามารถใช้ [Multichain](https://multichain.org/) (เดิมเป็น AnySwap) เพื่อเชื่อมต่อโทเค็นระหว่างเครือข่ายที่พบบ่อยที่สุด


**โปรดทราบว่าการที่จะเชื่อมต่อโทเค็น คุณจะต้องมีเงินทุนใน Native Token ของเครือข่ายเพื่อที่จะจ่ายเงินค่าธรรมเนียมแก๊ส** ซึ่งเป็นสิ่งจำเป็นสำหรับทุกการทำธุรกรรมตัวอย่างเช่น บน BSC คุณจะต้องมี BNB บน Polygon คุณจะมี MATIC และสำหรับ Avalanche คุณจะต้องมี AVAX

