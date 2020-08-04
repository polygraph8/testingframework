from mitmproxy.utils import strutils
from mitmproxy import ctx
from mitmproxy import tcp


def tcp_message(flow: tcp.TCPFlow):
    message = flow.messages[-1]
    message.content = message.content.replace(b"foo", b"bar")

    ctx.log.info(
        f"tcp_message[from_client={message.from_client}), content={strutils.bytes_to_escaped_str(message.content)}]"
    )
    