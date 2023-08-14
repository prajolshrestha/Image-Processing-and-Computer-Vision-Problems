% Derivative- based Time series segmentaion

% learn: zscore,cumsum,conv,diff,nan

%% 

clear
N = 1000;
tv = (0:N-1)/30;

%gaussian window
gwin = exp(-zscore(tv).^2/.0001);

% 'stock market' : smoothed noise + linear trend
signal = conv(cumsum(randn(N,1)),gwin,'same') + linspace(-100,100,N)';

%compute derivative
signalD = diff(signal);
signalD(N) = signalD(end);

figure(1),clf
subplot(311)
plot(tv(1:end),signal)
title('Original Signal')
subplot(312)
plot(tv(1:end),signalD,'r')
title('Derivative of signal')
subplot(313)
hist(zscore(signalD),150)
title('Histogram')


%% Select Threshold based on normalized derivative

zthresh = 1.7;

% Find extreme derivative points up and down
deriv_hi = find(zscore(signalD) > zthresh);
deriv_lo = find(zscore(signalD) < -zthresh);

% create new time series of NaN's with selected time points
jumpUp = nan(N,1);
jumpUp(deriv_hi) = signal(deriv_hi);

jumpDn = nan(N,1);
jumpDn(deriv_lo) = signal(deriv_lo);

figure(2),clf,hold on
plot(tv,signal,'k')
plot(tv,jumpUp,'g','LineWidth',3)
plot(tv,jumpDn,'r','LineWidth',3)

set(gca,'xlim',tv([1 end]),'xtick',0:6:max(tv),'ytick',[])
legend({'Stock market';'Good Times';'Bad Times'})
title(['Stock market values with shifts at ' num2str(zthresh) ' std indicater'])












