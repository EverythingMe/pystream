import click
import smart_open


class SmartFile(click.File):
    """
    The convenience of click.File with the power of smart_open.

    If smart_open detects the file as file:// scheme, use the default click.File (accepts "-" for stdin/stdout)
    Otherwise, open it with smart_open
    """

    def convert(self, value, param, ctx):
        uri = smart_open.ParseUri(value)

        if uri.scheme == 'file':
            return super(SmartFile, self).convert(uri.uri_path, param, ctx)
        else:
            return smart_open.smart_open(value, self.mode)


@click.command()
@click.option('--chunk-size', default=8192)
@click.argument('src', type=SmartFile('rb'))
@click.argument('dst', type=SmartFile('wb'))
def main(chunk_size, src, dst):
    while True:
        chunk = src.read(chunk_size)

        if len(chunk) == 0:
            break

        dst.write(chunk)

    dst.close()


if __name__ == '__main__':
    main()
