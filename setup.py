import setuptools
import platform
from distutils import sysconfig
from distutils import version
import os
import sys

# below is just all the sources listed in freeimage's Makefile.srcs, less the JXR stuff
# which is breaking on some windows builds and I have no idea how to fix it, so out it goes.
SRCS = '''
Source/FreeImage/BitmapAccess.cpp
Source/FreeImage/ColorLookup.cpp
Source/FreeImage/ConversionRGBA16.cpp
Source/FreeImage/ConversionRGBAF.cpp
Source/FreeImage/FreeImage.cpp
Source/FreeImage/FreeImageC.c
Source/FreeImage/FreeImageIO.cpp
Source/FreeImage/GetType.cpp
Source/FreeImage/LFPQuantizer.cpp
Source/FreeImage/MemoryIO.cpp
Source/FreeImage/PixelAccess.cpp
Source/FreeImage/J2KHelper.cpp
Source/FreeImage/MNGHelper.cpp
Source/FreeImage/Plugin.cpp
Source/FreeImage/PluginBMP.cpp
Source/FreeImage/PluginCUT.cpp
Source/FreeImage/PluginDDS.cpp
Source/FreeImage/PluginG3.cpp
Source/FreeImage/PluginGIF.cpp
Source/FreeImage/PluginHDR.cpp
Source/FreeImage/PluginICO.cpp
Source/FreeImage/PluginIFF.cpp
Source/FreeImage/PluginJ2K.cpp
Source/FreeImage/PluginJNG.cpp
Source/FreeImage/PluginJP2.cpp
Source/FreeImage/PluginJPEG.cpp
Source/FreeImage/PluginKOALA.cpp
Source/FreeImage/PluginMNG.cpp
Source/FreeImage/PluginPCD.cpp
Source/FreeImage/PluginPCX.cpp
Source/FreeImage/PluginPFM.cpp
Source/FreeImage/PluginPICT.cpp
Source/FreeImage/PluginPNG.cpp
Source/FreeImage/PluginPNM.cpp
Source/FreeImage/PluginPSD.cpp
Source/FreeImage/PluginRAS.cpp
Source/FreeImage/PluginRAW.cpp
Source/FreeImage/PluginSGI.cpp
Source/FreeImage/PluginTARGA.cpp
Source/FreeImage/PluginTIFF.cpp
Source/FreeImage/PluginWBMP.cpp
Source/FreeImage/PluginWebP.cpp
Source/FreeImage/PluginXBM.cpp
Source/FreeImage/PluginXPM.cpp
Source/FreeImage/PSDParser.cpp
Source/FreeImage/TIFFLogLuv.cpp
Source/FreeImage/Conversion.cpp
Source/FreeImage/Conversion16_555.cpp
Source/FreeImage/Conversion16_565.cpp
Source/FreeImage/Conversion24.cpp
Source/FreeImage/Conversion32.cpp
Source/FreeImage/Conversion4.cpp
Source/FreeImage/Conversion8.cpp
Source/FreeImage/ConversionFloat.cpp
Source/FreeImage/ConversionRGB16.cpp
Source/FreeImage/ConversionRGBF.cpp
Source/FreeImage/ConversionType.cpp
Source/FreeImage/ConversionUINT16.cpp
Source/FreeImage/Halftoning.cpp
Source/FreeImage/tmoColorConvert.cpp
Source/FreeImage/tmoDrago03.cpp
Source/FreeImage/tmoFattal02.cpp
Source/FreeImage/tmoReinhard05.cpp
Source/FreeImage/ToneMapping.cpp
Source/FreeImage/NNQuantizer.cpp
Source/FreeImage/WuQuantizer.cpp
Source/FreeImage/CacheFile.cpp
Source/FreeImage/MultiPage.cpp
Source/FreeImage/ZLibInterface.cpp
Source/Metadata/Exif.cpp
Source/Metadata/FIRational.cpp
Source/Metadata/FreeImageTag.cpp
Source/Metadata/IPTC.cpp
Source/Metadata/TagConversion.cpp
Source/Metadata/TagLib.cpp
Source/Metadata/XTIFF.cpp
Source/FreeImageToolkit/Background.cpp
Source/FreeImageToolkit/BSplineRotate.cpp
Source/FreeImageToolkit/Channels.cpp
Source/FreeImageToolkit/ClassicRotate.cpp
Source/FreeImageToolkit/Colors.cpp
Source/FreeImageToolkit/CopyPaste.cpp
Source/FreeImageToolkit/Display.cpp
Source/FreeImageToolkit/Flip.cpp
Source/FreeImageToolkit/JPEGTransform.cpp
Source/FreeImageToolkit/MultigridPoissonSolver.cpp
Source/FreeImageToolkit/Rescale.cpp
Source/FreeImageToolkit/Resize.cpp
Source/LibJPEG/jaricom.c
Source/LibJPEG/jcapimin.c
Source/LibJPEG/jcapistd.c
Source/LibJPEG/jcarith.c
Source/LibJPEG/jccoefct.c
Source/LibJPEG/jccolor.c
Source/LibJPEG/jcdctmgr.c
Source/LibJPEG/jchuff.c
Source/LibJPEG/jcinit.c
Source/LibJPEG/jcmainct.c
Source/LibJPEG/jcmarker.c
Source/LibJPEG/jcmaster.c
Source/LibJPEG/jcomapi.c
Source/LibJPEG/jcparam.c
Source/LibJPEG/jcprepct.c
Source/LibJPEG/jcsample.c
Source/LibJPEG/jctrans.c
Source/LibJPEG/jdapimin.c
Source/LibJPEG/jdapistd.c
Source/LibJPEG/jdarith.c
Source/LibJPEG/jdatadst.c
Source/LibJPEG/jdatasrc.c
Source/LibJPEG/jdcoefct.c
Source/LibJPEG/jdcolor.c
Source/LibJPEG/jddctmgr.c
Source/LibJPEG/jdhuff.c
Source/LibJPEG/jdinput.c
Source/LibJPEG/jdmainct.c
Source/LibJPEG/jdmarker.c
Source/LibJPEG/jdmaster.c
Source/LibJPEG/jdmerge.c
Source/LibJPEG/jdpostct.c
Source/LibJPEG/jdsample.c
Source/LibJPEG/jdtrans.c
Source/LibJPEG/jerror.c
Source/LibJPEG/jfdctflt.c
Source/LibJPEG/jfdctfst.c
Source/LibJPEG/jfdctint.c
Source/LibJPEG/jidctflt.c
Source/LibJPEG/jidctfst.c
Source/LibJPEG/jidctint.c
Source/LibJPEG/jmemmgr.c
Source/LibJPEG/jmemnobs.c
Source/LibJPEG/jquant1.c
Source/LibJPEG/jquant2.c
Source/LibJPEG/jutils.c
Source/LibJPEG/transupp.c
Source/LibPNG/png.c
Source/LibPNG/pngerror.c
Source/LibPNG/pngget.c
Source/LibPNG/pngmem.c
Source/LibPNG/pngpread.c
Source/LibPNG/pngread.c
Source/LibPNG/pngrio.c
Source/LibPNG/pngrtran.c
Source/LibPNG/pngrutil.c
Source/LibPNG/pngset.c
Source/LibPNG/pngtrans.c
Source/LibPNG/pngwio.c
Source/LibPNG/pngwrite.c
Source/LibPNG/pngwtran.c
Source/LibPNG/pngwutil.c
Source/LibTIFF4/tif_aux.c
Source/LibTIFF4/tif_close.c
Source/LibTIFF4/tif_codec.c
Source/LibTIFF4/tif_color.c
Source/LibTIFF4/tif_compress.c
Source/LibTIFF4/tif_dir.c
Source/LibTIFF4/tif_dirinfo.c
Source/LibTIFF4/tif_dirread.c
Source/LibTIFF4/tif_dirwrite.c
Source/LibTIFF4/tif_dumpmode.c
Source/LibTIFF4/tif_error.c
Source/LibTIFF4/tif_extension.c
Source/LibTIFF4/tif_fax3.c
Source/LibTIFF4/tif_fax3sm.c
Source/LibTIFF4/tif_flush.c
Source/LibTIFF4/tif_getimage.c
Source/LibTIFF4/tif_jpeg.c
Source/LibTIFF4/tif_luv.c
Source/LibTIFF4/tif_lzma.c
Source/LibTIFF4/tif_lzw.c
Source/LibTIFF4/tif_next.c
Source/LibTIFF4/tif_ojpeg.c
Source/LibTIFF4/tif_open.c
Source/LibTIFF4/tif_packbits.c
Source/LibTIFF4/tif_pixarlog.c
Source/LibTIFF4/tif_predict.c
Source/LibTIFF4/tif_print.c
Source/LibTIFF4/tif_read.c
Source/LibTIFF4/tif_strip.c
Source/LibTIFF4/tif_swab.c
Source/LibTIFF4/tif_thunder.c
Source/LibTIFF4/tif_tile.c
Source/LibTIFF4/tif_version.c
Source/LibTIFF4/tif_warning.c
Source/LibTIFF4/tif_write.c
Source/LibTIFF4/tif_zip.c
Source/ZLib/adler32.c
Source/ZLib/compress.c
Source/ZLib/crc32.c
Source/ZLib/deflate.c
Source/ZLib/gzclose.c
Source/ZLib/gzlib.c
Source/ZLib/gzread.c
Source/ZLib/gzwrite.c
Source/ZLib/infback.c
Source/ZLib/inffast.c
Source/ZLib/inflate.c
Source/ZLib/inftrees.c
Source/ZLib/trees.c
Source/ZLib/uncompr.c
Source/ZLib/zutil.c
Source/LibOpenJPEG/bio.c
Source/LibOpenJPEG/cio.c
Source/LibOpenJPEG/dwt.c
Source/LibOpenJPEG/event.c
Source/LibOpenJPEG/function_list.c
Source/LibOpenJPEG/image.c
Source/LibOpenJPEG/invert.c
Source/LibOpenJPEG/j2k.c
Source/LibOpenJPEG/jp2.c
Source/LibOpenJPEG/mct.c
Source/LibOpenJPEG/mqc.c
Source/LibOpenJPEG/openjpeg.c
Source/LibOpenJPEG/opj_clock.c
Source/LibOpenJPEG/pi.c
Source/LibOpenJPEG/raw.c
Source/LibOpenJPEG/t1.c
Source/LibOpenJPEG/t2.c
Source/LibOpenJPEG/tcd.c
Source/LibOpenJPEG/tgt.c
Source/LibRawLite/internal/dcraw_common.cpp
Source/LibRawLite/internal/dcraw_fileio.cpp
Source/LibRawLite/internal/demosaic_packs.cpp
Source/LibRawLite/src/libraw_c_api.cpp
Source/LibRawLite/src/libraw_cxx.cpp
Source/LibRawLite/src/libraw_datastream.cpp
Source/LibWebP/src/dec/alpha_dec.c
Source/LibWebP/src/dec/buffer_dec.c
Source/LibWebP/src/dec/frame_dec.c
Source/LibWebP/src/dec/idec_dec.c
Source/LibWebP/src/dec/io_dec.c
Source/LibWebP/src/dec/quant_dec.c
Source/LibWebP/src/dec/tree_dec.c
Source/LibWebP/src/dec/vp8l_dec.c
Source/LibWebP/src/dec/vp8_dec.c
Source/LibWebP/src/dec/webp_dec.c
Source/LibWebP/src/demux/anim_decode.c
Source/LibWebP/src/demux/demux.c
Source/LibWebP/src/dsp/alpha_processing.c
Source/LibWebP/src/dsp/alpha_processing_mips_dsp_r2.c
Source/LibWebP/src/dsp/alpha_processing_neon.c
Source/LibWebP/src/dsp/alpha_processing_sse2.c
Source/LibWebP/src/dsp/alpha_processing_sse41.c
Source/LibWebP/src/dsp/cost.c
Source/LibWebP/src/dsp/cost_mips32.c
Source/LibWebP/src/dsp/cost_mips_dsp_r2.c
Source/LibWebP/src/dsp/cost_neon.c
Source/LibWebP/src/dsp/cost_sse2.c
Source/LibWebP/src/dsp/cpu.c
Source/LibWebP/src/dsp/dec.c
Source/LibWebP/src/dsp/dec_clip_tables.c
Source/LibWebP/src/dsp/dec_mips32.c
Source/LibWebP/src/dsp/dec_mips_dsp_r2.c
Source/LibWebP/src/dsp/dec_msa.c
Source/LibWebP/src/dsp/dec_neon.c
Source/LibWebP/src/dsp/dec_sse2.c
Source/LibWebP/src/dsp/dec_sse41.c
Source/LibWebP/src/dsp/enc.c
Source/LibWebP/src/dsp/enc_avx2.c
Source/LibWebP/src/dsp/enc_mips32.c
Source/LibWebP/src/dsp/enc_mips_dsp_r2.c
Source/LibWebP/src/dsp/enc_msa.c
Source/LibWebP/src/dsp/enc_neon.c
Source/LibWebP/src/dsp/enc_sse2.c
Source/LibWebP/src/dsp/enc_sse41.c
Source/LibWebP/src/dsp/filters.c
Source/LibWebP/src/dsp/filters_mips_dsp_r2.c
Source/LibWebP/src/dsp/filters_msa.c
Source/LibWebP/src/dsp/filters_neon.c
Source/LibWebP/src/dsp/filters_sse2.c
Source/LibWebP/src/dsp/lossless.c
Source/LibWebP/src/dsp/lossless_enc.c
Source/LibWebP/src/dsp/lossless_enc_mips32.c
Source/LibWebP/src/dsp/lossless_enc_mips_dsp_r2.c
Source/LibWebP/src/dsp/lossless_enc_msa.c
Source/LibWebP/src/dsp/lossless_enc_neon.c
Source/LibWebP/src/dsp/lossless_enc_sse2.c
Source/LibWebP/src/dsp/lossless_enc_sse41.c
Source/LibWebP/src/dsp/lossless_mips_dsp_r2.c
Source/LibWebP/src/dsp/lossless_msa.c
Source/LibWebP/src/dsp/lossless_neon.c
Source/LibWebP/src/dsp/lossless_sse2.c
Source/LibWebP/src/dsp/rescaler.c
Source/LibWebP/src/dsp/rescaler_mips32.c
Source/LibWebP/src/dsp/rescaler_mips_dsp_r2.c
Source/LibWebP/src/dsp/rescaler_msa.c
Source/LibWebP/src/dsp/rescaler_neon.c
Source/LibWebP/src/dsp/rescaler_sse2.c
Source/LibWebP/src/dsp/ssim.c
Source/LibWebP/src/dsp/ssim_sse2.c
Source/LibWebP/src/dsp/upsampling.c
Source/LibWebP/src/dsp/upsampling_mips_dsp_r2.c
Source/LibWebP/src/dsp/upsampling_msa.c
Source/LibWebP/src/dsp/upsampling_neon.c
Source/LibWebP/src/dsp/upsampling_sse2.c
Source/LibWebP/src/dsp/upsampling_sse41.c
Source/LibWebP/src/dsp/yuv.c
Source/LibWebP/src/dsp/yuv_mips32.c
Source/LibWebP/src/dsp/yuv_mips_dsp_r2.c
Source/LibWebP/src/dsp/yuv_neon.c
Source/LibWebP/src/dsp/yuv_sse2.c
Source/LibWebP/src/dsp/yuv_sse41.c
Source/LibWebP/src/enc/alpha_enc.c
Source/LibWebP/src/enc/analysis_enc.c
Source/LibWebP/src/enc/backward_references_cost_enc.c
Source/LibWebP/src/enc/backward_references_enc.c
Source/LibWebP/src/enc/config_enc.c
Source/LibWebP/src/enc/cost_enc.c
Source/LibWebP/src/enc/filter_enc.c
Source/LibWebP/src/enc/frame_enc.c
Source/LibWebP/src/enc/histogram_enc.c
Source/LibWebP/src/enc/iterator_enc.c
Source/LibWebP/src/enc/near_lossless_enc.c
Source/LibWebP/src/enc/picture_csp_enc.c
Source/LibWebP/src/enc/picture_enc.c
Source/LibWebP/src/enc/picture_psnr_enc.c
Source/LibWebP/src/enc/picture_rescale_enc.c
Source/LibWebP/src/enc/picture_tools_enc.c
Source/LibWebP/src/enc/predictor_enc.c
Source/LibWebP/src/enc/quant_enc.c
Source/LibWebP/src/enc/syntax_enc.c
Source/LibWebP/src/enc/token_enc.c
Source/LibWebP/src/enc/tree_enc.c
Source/LibWebP/src/enc/vp8l_enc.c
Source/LibWebP/src/enc/webp_enc.c
Source/LibWebP/src/mux/anim_encode.c
Source/LibWebP/src/mux/muxedit.c
Source/LibWebP/src/mux/muxinternal.c
Source/LibWebP/src/mux/muxread.c
Source/LibWebP/src/utils/bit_reader_utils.c
Source/LibWebP/src/utils/bit_writer_utils.c
Source/LibWebP/src/utils/color_cache_utils.c
Source/LibWebP/src/utils/filters_utils.c
Source/LibWebP/src/utils/huffman_encode_utils.c
Source/LibWebP/src/utils/huffman_utils.c
Source/LibWebP/src/utils/quant_levels_dec_utils.c
Source/LibWebP/src/utils/quant_levels_utils.c
Source/LibWebP/src/utils/random_utils.c
Source/LibWebP/src/utils/rescaler_utils.c
Source/LibWebP/src/utils/thread_utils.c
Source/LibWebP/src/utils/utils.c
Source/OpenEXR/Half/half.cpp
'''.strip().split()

INCLUDE = '''
Source
Source/Metadata
Source/FreeImageToolkit
Source/LibJPEG
Source/LibPNG
Source/LibTIFF4
Source/ZLib
Source/LibOpenJPEG
Source/LibRawLite
Source/LibRawLite/dcraw
Source/LibRawLite/internal
Source/LibRawLite/libraw
Source/LibRawLite/src
Source/LibWebP
Source/OpenEXR
'''.strip().split()

# For mac, ensure extensions are built for macos 10.9 when compiling on a
# 10.9 system or above, overriding distuitls behaviour which is to target
# the version that python was built for. This may be overridden by setting
# MACOSX_DEPLOYMENT_TARGET before calling setup.py
# If below is not included, or 10.14 and above, the C++ standard headers may
# not be found.
extra_compile_args = []
if sys.platform == 'darwin':
    if 'MACOSX_DEPLOYMENT_TARGET' not in os.environ:
        current_system = version.LooseVersion(platform.mac_ver()[0])
        python_target = version.LooseVersion(sysconfig.get_config_var('MACOSX_DEPLOYMENT_TARGET'))
        if python_target < '10.9' and current_system >= '10.9':
            os.environ['MACOSX_DEPLOYMENT_TARGET'] = '10.9'
        extra_compile_args.append('-Wno-error=implicit-function-declaration')

freeimage = setuptools.Extension(
    name='freeimage._freeimage',
    sources=['freeimage/_freeimage.c'] + SRCS,
    include_dirs=INCLUDE,
    define_macros=[('__ANSI__', None), ('NO_LCMS', None), ('DISABLE_PERF_MEASUREMENT', None), ('PNG_ARM_NEON_OPT', 0)],
    extra_compile_args=extra_compile_args
)

setuptools.setup(
    name='freeimage',
    version='1.2',
    description='freeimage package',
    ext_modules=[freeimage],
    packages=setuptools.find_packages()
)
