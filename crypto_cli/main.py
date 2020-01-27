import sys
import click

from crypto_cli.chiper import chiper_list


@click.group(chain=True)
@click.option(
    "-r",
    "--reverse",
    is_flag=True,
    default=False,
    help="Reverse the order of the chipers",
)
def cli(reverse):
    """
    A basic crypto cli tools.
    """
    pass


def gen(op):
    @cli.command(op, help=f"Set operation to '{op}'")
    def command():
        def processor(ctx):
            ctx["op"] = op
            return ctx

        return processor


for op in ["encode", "decode"]:
    gen(op)


@cli.resultcallback()
def process_cli(processors, reverse):
    ctx = {"chipers": []}
    for processor in processors:
        # print(processor)
        ctx = processor(ctx)
    # print(f"{ctx=}")

    ctx["input"] = sys.stdin.buffer
    ctx["output"] = sys.stdout.buffer

    message = ctx["input"].read()

    # print(f"{message=}")
    # print(f"{reverse=}")
    if reverse:
        ctx["chipers"].reverse()

    for chiper in ctx["chipers"]:
        if ctx["op"] == "encode":
            message = chiper.encode(message)
        elif ctx["op"] == "decode":
            message = chiper.decode(message)

    # print(f"{message=}")
    ctx["output"].write(message)
    ctx["output"].close()


for chiper in chiper_list:
    cli.add_command(chiper.command)


def main():
    cli()


if __name__ == "__main__":
    main()
